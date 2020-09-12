from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserInfo


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    fields = (
        'default_email',
        'first_name',
        'last_name',
        'default_phone_number',
        'default_street_address_1',
        'default_street_address_2',
        'default_town_or_city',
        'default_state',
        'default_postcode',
    )
    
    list_display = (
        'first_name',
        'last_name',
        'default_email',
    )

    ordering = ('last_name',)

admin.site.register(UserInfo, ProfileAdmin)