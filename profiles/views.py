from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserInfo, UserDeliveryInfo
from .forms import UserInfoForm, UserDeliveryInfoForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    user = request.user
    user_info = get_object_or_404(UserInfo, user=user)
    delivery_info = get_object_or_404(UserDeliveryInfo, user=user)
    
    # Populate forms with user's information
    user_info_form = UserInfoForm(instance=user_info)
    delivery_info_form = UserDeliveryInfoForm(instance=delivery_info)

    orders = user_info.orders.all()

    template = 'profiles/profile.html'
    context = {
        
        'user': user,
        'user_info_form': user_info_form,
        'delivery_info_form': delivery_info_form,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)