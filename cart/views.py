from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view that renders all cart items """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    grind = request.POST.get('grind')
    redirect_url = request.POST.get('redirect_url')

    if grind == 'none':
        messages.error(request, 'Please select a grind option!')
    else:
        cart = request.session.get('cart', {})
        if item_id in list(cart.keys()):
            if grind in cart[item_id]['product_by_grind'].keys():
                cart[item_id]['product_by_grind'][grind] += quantity
            else:
                cart[item_id]['product_by_grind'][grind] = quantity
        else:
            cart[item_id] = {'product_by_grind': {grind: quantity}}
        
        print(cart)
        request.session['cart'] = cart
    
    return redirect(redirect_url)