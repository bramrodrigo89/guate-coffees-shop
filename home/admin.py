from django.contrib import admin
from .models import CustomerInquiry

# Register your models here.


class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'user',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'description',
        'created_at',
    )
    ordering = ('-created_at',)


admin.site.register(CustomerInquiry, CustomerInquiryAdmin)
