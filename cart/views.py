from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


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
        
        request.session['cart'] = cart
    
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update item quantities in cart and delete them if requested """

    quantity = int(request.POST.get('quantity'))
    grind = request.POST.get('grind')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id]['product_by_grind'][grind] = quantity
    else:
        del cart[item_id]['product_by_grind'][grind]
        if not cart[item_id]['product_by_grind']:
            cart.pop(item_id)

    request.session['cart'] = cart
    
    return redirect(reverse(view_cart))


def remove_from_cart(request, item_id):
    """ Remove items from cart when requested """
    
    try:
        grind = request.POST.get('grind')
        cart = request.session.get('cart', {})

        del cart[item_id]['product_by_grind'][grind]
        print('maybe here?')
        if not cart[item_id]['product_by_grind']:
            cart.pop(item_id)

        request.session['cart'] = cart
        
        return HttpResponse(status=200)

    except Exception as e:
        print('at least i came here')
        return HttpResponse(status=500)