from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send_inquiry', views.send_inquiry, name='send_inquiry'),
]
