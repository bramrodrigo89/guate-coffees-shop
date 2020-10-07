from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserInfo

import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks after payments are processed
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send an order confirmation email"""
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Correct format of data in shipping details received from webhook
        for field, value in shipping.address.items():
            if value == "":
                shipping.address[field] = None

        # Update profile information if save_info was checked
        user_info = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_info = UserInfo.objects.get(user__username=username)
            if save_info is True:
                user_info.first_name = shipping.name.split(", ")[1]
                user_info.last_name = shipping.name.split(", ")[0]
                user_info.default_email = billing_details.email
                user_info.default_phone_number = shipping.phone
                user_info.default_postcode = shipping.address.postal_code
                user_info.default_town_or_city = shipping.address.city
                user_info.default_street_address_1 = shipping.address.line1
                user_info.default_street_address_2 = shipping.address.line2
                user_info.default_state = shipping.address.state
                user_info.default_country = shipping.address.country
                user_info.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping.name.split(", ")[1],
                    last_name__iexact=shipping.name.split(", ")[0],
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=shipping.address.country,
                    postcode__iexact=shipping.address.postal_code,
                    town_or_city__iexact=shipping.address.city,
                    street_address_1__iexact=shipping.address.line1,
                    street_address_2__iexact=shipping.address.line2,
                    state__iexact=shipping.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            # Send confirmation email at point of being sure order was received
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order saved in database already before webhook',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping.name.split(", ")[1],
                    last_name=shipping.name.split(", ")[0],
                    username=user_info,
                    email=billing_details.email,
                    phone_number=shipping.phone,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    town_or_city=shipping.address.city,
                    street_address_1=shipping.address.line1,
                    street_address_2=shipping.address.line2,
                    state=shipping.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    for grind, qty in item_data['product_by_grind'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=qty,
                            product_grind=grind,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Send confirmation email at point of being sure order was received
        self._send_confirmation_email(order)
        if 'cart' in self.request.session:
            del self.request.session['cart']
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order after webhook',
            status=200)

    def handle_event(self, event):
        """
        Handle all other types of webhook events
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
