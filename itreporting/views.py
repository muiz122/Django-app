from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect
# from .forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html')


# Function-based view for About
def about(request):
    return render(request, 'itreporting/about.html')

# Function-based view for Contact
def contact(request):
    return render(request, 'itreporting/contact.html')
    
