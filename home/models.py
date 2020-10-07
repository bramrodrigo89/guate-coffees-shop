from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your models here.


class CustomerInquiry(models.Model):
    category = models.CharField(max_length=10, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    user = models.ForeignKey(
      User, on_delete=models.SET_NULL, null=True,
      blank=True, related_name='inquiries')
    description = models.TextField(
        default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category} sent by {self.user}'

    def _send_confirmation_email(self, form):
        """Send an order confirmation email"""
        customer_email = form.email
        subject = render_to_string(
            'home/confirmation_emails/confirmation_email_subject.txt',
            {'form': form})
        body = render_to_string(
            'home/confirmation_emails/confirmation_email_body.txt',
            {'form': form, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
