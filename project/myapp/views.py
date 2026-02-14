from django.shortcuts import render

# Create your views here.
def landing(req):
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
     
      
      
                                                