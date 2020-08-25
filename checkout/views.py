from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_items

import stripe

def checkout(request):
    """
    Create Payment Intent session at the beginning and rendering the checkout template with information needed for stripe payments
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_public_key:
        messages.warning(request, 'Public Key is missing in environment! Please add Stripe Public Key')

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