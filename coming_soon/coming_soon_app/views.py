from django.shortcuts import render
from .models import NewsletterSignup
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'coming_soon_app\index.html')

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSignup.objects.create(email=email)
            return HttpResponse("Thank you for signing up!")
    return render(request, 'newsletter.html')