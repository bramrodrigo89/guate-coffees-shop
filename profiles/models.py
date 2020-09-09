from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

class UserInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Profiles Data'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user personal information
    """
    if created:
        UserInfo.objects.create(user=instance)
    # For existing users: just save the profile
    instance.userinfo.save()

class UserDeliveryInfo(models.Model):
    """
    A user profile model for maintaining default delivery information, order history and reviews history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address_1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_state = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserDeliveryInfo.objects.create(user=instance)
    # For existing users: just save the profile
    instance.UserDeliveryInfo.save()


