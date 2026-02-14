from django.shortcuts import render

# Create your views here.
def landing(req):
<<<<<<< HEAD
   return render(req,'landing.html')

def set(req):
    return render(req,'set.html')

def set_data(req):
 if req.method=='POST':
    n=req.POST.get('name')
    e=req.POST.get('email')
    print(n,e)
    req.session['name']=n
    req.session['email']=e
    return render(req,'landing.html',{'msg':"Date set succesfully"})
 
def get_data(req):
   n=req.session.get('name')
   e=req.session.get('email')
   data={'name':n,'email':e}
   return render(req,'landing.html',{'data':data,'msg1':"Get data from session"})

def delete_data(req):
   if req.session.get('name') and req.session.get('email'):
    del req.session['name']
    del req.session['email']
    #
    return render(req,'landing.html',{'msg2':"data_deleted"})
   else:
     return render(req,'landing.html',{'msg2':"data not found"})
     
      
      
                                                
=======
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
>>>>>>> fdc7b92f5dfacec0c5d5d482cb38ef15f9c80442
