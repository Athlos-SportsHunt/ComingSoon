from django.shortcuts import render, redirect
from .models import *   
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'coming_soon_app/index.html')

def submit_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                Updates.objects.create(email=email)
                return redirect('coming_soon_app:home')
            except IntegrityError:
                return HttpResponse("This email has already been used.")
    return redirect('coming_soon_app:home')
