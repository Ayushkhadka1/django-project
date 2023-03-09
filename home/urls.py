from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('contactus', contact, name='contactus'),
    path('aboutus', about, name='aboutus'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
]
