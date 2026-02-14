from django.shortcuts import render
import random

# Create your views here.
from django.core.mail import send_mail

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )
#  password=>  khtn jgqb syne lhka
#def landing(req):
  # return render(req,'landing.html')

def my_render(req):
    return render(req,'landing.html')

def send_otp(req):
    if req.method=='POST':
        e=req.POST.get('email')
        otp=random.randint(111111,999999)
        req.session['email'],req.session['otp']=e,otp
        send_mail(
                  'OTP from Django aPP',
                   f'your OTP is {'otp'}',
                  'goursonoo16@gmail.com',
                   [e],
                   fail_silently=False,)
                         
        return render(req,'landing.html',{'msg':'otp send succcessfully'})

                       