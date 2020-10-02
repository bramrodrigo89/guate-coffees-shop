from .forms import CustomerInquiryForm
from .models import CustomerInquiry
from profiles.models import UserInfo


def customer_inquiry_form(request):
    inquiry = CustomerInquiry()
    inquiry_form = CustomerInquiryForm()

    # If user is logged in, profile information can be
    # retrieved for modal form
    if request.user.is_authenticated:
        try:
            user_info = UserInfo.objects.get(user=request.user)
            inquiry_form = CustomerInquiryForm(initial={
                'first_name': user_info.first_name,
                'last_name': user_info.last_name,
                'email': user_info.default_email,
                'phone_number': user_info.default_phone_number,
            })
        except UserInfo.DoesNotExist:
            inquiry_form = CustomerInquiryForm()
    else:
        inquiry_form = CustomerInquiryForm()

    context = {
        'inquiry_form': inquiry_form,
        'inquiry': inquiry
    }

    return context
