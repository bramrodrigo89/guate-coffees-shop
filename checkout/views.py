from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from cart.contexts import cart_items

import stripe
import json

@require_POST
def cache_checkout_data(request):
    """
    Add information from order to metadata during stripe payment intent
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Create Payment Intent session at the beginning and rendering the checkout template with information needed for stripe payments
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'username': request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'state': request.POST['state'],
        }
        # create new instance of OrderForm
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save(commit=True)
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    for grind, quantity in item_data['product_by_grind'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_grind=grind,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your bag no longer exists in our store. Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Something went wrong with the information you provided. Please try again!')
            return redirect(reverse('checkout'))
    else:
        # Everything else
        if not stripe_public_key:
            messages.warning(request, 'Public Key is missing in environment! Please add Stripe Public Key')
            return redirect(reverse('checkout_success', args=[order.order_number]))

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'There is nothing in your cart at this time')
            return redirect(reverse('products'))
        
        current_cart = cart_items(request)
        total = current_cart['grand_total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, 'Order successfully processed!')

    if 'cart' in request.session:
        del request.session['cart']

    new_products = Product.objects.filter(new_product=True)
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_number': order_number,
        'email_address': order.email,
        'new_products': new_products,
    }

    return render(request, template, context)