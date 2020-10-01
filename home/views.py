
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
        inquiry_form = CustomerInquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry = inquiry_form.save(commit=False)
            inquiry.user = user
            inquiry.save()
            messages.success(
                request, 'Thank you! Your inquiry was sent successfully!'
            )
        else:
            messages.error(
                request, 'Sorry! Please ensure the form is valid.'
            )
    
    return render(request, 'home/index.html')

