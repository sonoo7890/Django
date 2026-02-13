from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'base.html')

def my_home(req):
    data={'name':'sonu'}
    return render(req,'home.html',data)
#return render(req,'home.html',{'name':'sonu' name1:})

def my_about(req):
    
    return render(req,'about.html')

def my_contact(req):
    
    return render(req,'contact.html')

def my_registration(req):
    
    return render(req,'registration.html')


def my_login(req):
    
    return render(req,'login.html')


def my_services(req):
    data={'name':'sonu'}
    return render(req,'services.html',data)
