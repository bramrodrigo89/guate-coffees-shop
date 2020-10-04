
from django.shortcuts import render, redirect
from .models import CustomerInquiry
from django.contrib import messages
from .forms import CustomerInquiryForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def send_inquiry(request):
    """ A view to send an inquiry using the contact modal """
    if request.method == 'POST':
        user = request.user
        redirect_url = request.POST.get('redirect_url')
        inquiry_data = {
            'category': request.POST.get('category_selector'),
            'user': user,
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'description': request.POST['description'],
        }
        inquiry_form = CustomerInquiryForm(inquiry_data)
        if inquiry_form.is_valid():
            inquiry = inquiry_form.save()
            inquiry._send_confirmation_email(inquiry)
            messages.success(
                request, 'Thank you! Your inquiry was sent successfully!'
            )
        else:
            messages.error(
                request, 'Sorry! Please ensure the form is valid.'
            )
    
    return redirect(redirect_url)

