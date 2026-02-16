from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(req):
    return render(req, 'home.html')
def about(req):
    return render(req, 'about.html')
def contact(req):
    return render(req, 'contact.html')
def products(req):
    products = Product.objects.all()
    return render(req, 'products.html', {'products': products})
def business(req):
    return render(req, 'bussiness.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def booking(request):
    return render(request, 'booking.html')
