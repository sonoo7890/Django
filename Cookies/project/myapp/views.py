from django.shortcuts import render

# Create your views here.
def landing(req):
    return render (req,'landing.html')
  
def  set(req):
    return render(req,'set.html')

def set_data(req):
 if req.method=='POST':
    n=req.POST.get('name')
    e=req.POST.get('email')
    print(n,e)
    response= render (req,'landing.html',{'msg':"Cookies set"})
    response.set_cookie('name',n,max_age=60*10)
    response.set_cookie('email',e)
    return response

def get_data(req):
   #print(req.COOKIES)
   if req.COOKIES:
      n=req.COOKIES.get('name')
      e=req.COOKIES.get('email')
      data={'name':n,'email':e}
      return render(req,'get.html',{'data':data})
   return render(req,'landing.html',{'msg':'Cookies not found'})

def delete_cookies(req):
  # if req.COOKIES['name'] and req.COOKIES['email'] :
   if req.COOKIES.get('name') and req.COOKIES.get('email'):

      response=render(req,'landing.html',{'msg1':"Cookies delete"})
      response.delete_cookie('name')
      response.delete_cookie('email')
      return response
   return render(req,'landing.html',{'msg1':"do not have cookies"})



                                        