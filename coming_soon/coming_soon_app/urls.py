from django.shortcuts import render
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('newsletter/', newsletter_signup, name='newsletter_signup'),
]


app_name = 'coming_soon_app'