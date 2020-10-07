from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from .forms import UserInfoForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.
    """
    user = request.user
    user_info = get_object_or_404(UserInfo, user=user)
    reviews = user.reviews.all()

    if request.method == 'POST':
        user_info_form = UserInfoForm(request.POST, instance=user_info)

        if user_info_form.is_valid():
            user_info_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed, please ensure \
                information entered is valid.')
    else:
        # Populate forms with user's information
        user_info_form = UserInfoForm(instance=user_info)

    orders = user_info.orders.all()

    template = 'profiles/profile.html'
    context = {
        'user': user,
        'user_info_form': user_info_form,
        'profile': profile,
        'orders': orders,
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the user's order history.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
