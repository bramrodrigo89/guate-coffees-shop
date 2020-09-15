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
    """Handle Stripe webhooks after payments are processed"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(content=f'Unhandled Webhook received: {event["type"]}', status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Correct format of data in shipping details received from webhook
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        user_info = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_info = UserInfo.objects.get(user__username=username)
            if save_info:
                user_info.default_phone_number = shipping_details.phone
                user_info.default_postcode = shipping_details.address.postal_code
                user_info.default_town_or_city = shipping_details.address.city
                user_info.default_street_address_1 = shipping_details.address.line1
                user_info.default_street_address_2 = shipping_details.address.line2
                user_info.default_state = shipping_details.address.state
                user_info.default_country = shipping_details.address.country
                user_info.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name.split(", ")[1],
                    last_name__iexact=shipping_details.name.split(", ")[0],
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    state__iexact=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            # self._send_confirmation_email(order)
            return HttpResponse(content=f'Webhook received: {event["type"]} | SUCCESS: Order saved in database already before webhook', status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name.split(", ")[1],
                    last_name=shipping_details.name.split(", ")[0],
                    username=user_info,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    state=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    for grind, quantity in item_data['product_by_grind'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_grind=grind,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500)
        
        # self._send_confirmation_email(order)
        return HttpResponse(content=f'Webhook received: {event["type"]} | SUCCESS: Created order after webhook', status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
