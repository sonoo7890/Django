# from django.shortcuts import render
# from.forms import RegForm
# # Create your views here.
# def home(req):
#     fm=RegForm()
#     return render(req,'home.html',{'form':fm})

from django.shortcuts import render, redirect
from .models import Aadhaar, Student


from django.shortcuts import render
from .forms import RegisterForm
#  path('',home,name='home')  from app.views import home
def home(request):
    if request.method == "POST":
        print("Hello...")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('Hii....') 
            print(form.cleaned_data)
            # form.save()
            return render(request, "success.html")
    else:
        form = RegisterForm()

    return render(request, "home.html", {"form": form})




def add_aadhaar(request):
    if request.method == 'POST':
        aadhaar_no = request.POST['aadhaar_no']
        name = request.POST['name']

        aadhaar = Aadhaar.objects.create(
            aadhaar_no=aadhaar_no,
            created_by=name
        )

        # Aadhaar save hone ke baad
        return redirect('add_student', aadhaar_id=aadhaar.id)

    return render(request, 'add_aadhaar.html')

def add_student(request, aadhaar_id):
    aadhaar = Aadhaar.objects.get(id=aadhaar_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']

        Student.objects.create(
            name=name,
            email=email,
            contact=contact,
            aadhaar=aadhaar
        )
        #  messages.success(request, "✅ Student saved successfully!")
        return redirect('add_student', aadhaar_id=aadhaar.id)
  

    return render(request, 'add_student.html', {'aadhaar': aadhaar})