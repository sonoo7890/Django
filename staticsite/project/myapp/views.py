from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def skills(request):
    return render(request, 'skills.html')

def career(request):
    return render(request, 'career.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')