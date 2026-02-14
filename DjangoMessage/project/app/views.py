from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def landing(req):
#    messages.info(req,'This is landing page')
   return render (req,'landing.html')
    #  return redirect('home')

def home(req):
    messages.info(req,'This is landing page')
    return render (req,'home.html')

def register(req):
    messages.info(req,'welcome to register page')
    return redirect(req,'register.html')