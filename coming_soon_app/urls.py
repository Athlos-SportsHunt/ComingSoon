from django.shortcuts import render
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('submit_email/', submit_email, name='submit_email'),
]


app_name = 'coming_soon_app'