from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
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

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # signup ke baad login page
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # DEMO LOGIN
        if username == "admin" and password == "12345":
            return redirect('dashboard')
        else:
            error = "Invalid Username or Password"

    return render(request, 'login.html', {'error': error})


def dashboard(request):
    return render(request, 'dashboard.html')


