from .forms import CustomerInquiryForm
from .models import CustomerInquiry


def customer_inquiry_form(request):
    inquiry = CustomerInquiry()
    inquiry_form = CustomerInquiryForm()
    context = {
        'inquiry_form': inquiry_form,
        'inquiry': inquiry
    }
    return context