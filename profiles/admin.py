from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserInfo


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    fields = (
        'user',
        'email',
        'first_name',
        'last_name',
    )
    
    list_display = (
        'user',
        'email',
        'first_name',
        'last_name',
    )

    ordering = ('user',)

admin.site.register(UserInfo, ProfileAdmin)