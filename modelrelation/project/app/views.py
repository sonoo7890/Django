from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentForm, AadharForm
from .models import Aadhar,Student,Employee,Department


def student(request):
    success = False
    all_adhars = Aadhar.objects.all()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = StudentForm()

    return render( request, "student.html", { "form": form,"success": success,"all_adhars": all_adhars
        }
    )


from .forms import AadharForm


def aadhar(request):
    if request.method == "POST":
        form = AadharForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = AadharForm()

    return render(request, "aadhar.html",{"form": form,"aadhar": True}
    )

def forword(req):
    ## One_To_One
    # # without related_name attribute
    # # first method
    # data=Student.objects.all()
    # print(data.query)
    # for i in data:
    #     print(i.name,i.email,i.contact,i.adhar_no.adhar_no,i.adhar_no.create_at)

    # # second method
    # data=Student.objects.select_related('adhar_no')
    # print(data.query)
    # for i in data:
    #     print(i.name,i.email,i.contact,i.adhar_no.adhar_no,i.adhar_no.create_at)
    
    ## One_To_Many--------------------------------
    ## first method
    # data = Employee.objects.all()
    # for i in data:
    #     print(i.e_dep.d_name,i.e_dep.d_hod)

    # second method
    data = Employee.objects.select_related('e_dep')
    for i in data:
        print(i.e_dep.d_name,i.e_dep.d_hod)

def reverse(req):
    
    ## One_To_One
    # without related_name attribute
    # data = Aadhar.objects.all()
    # print(data.query)
    # for i in data:
    #     print(i.adhar_no,i.create_at,i.student.name,i.student.email,i.student.contact)

    # data = Aadhar.objects.select_related('student')
    # print(data.query)
    # for i in data:
    #     print(i.adhar_no,i.create_at,i.student.name,i.student.email,i.student.contact)
    
    
    # data = Department.objects.all()
    # for i in data:
    #     print(i.d_name,i.d_hod,end=',')
    #     data1 = i.employee_set.all()
    #     for i in data1:
    #         print(i.e_name,i.e_email,i.e_contact)
    
    # data = Department.objects.prefetch_related('employee_set')
    # for i in data:
    #     print(i.d_name,i.d_hod,end=',')
    #     data1 = i.employee_set.all()
    #     for i in data1:
    #         print(i.e_name,i.e_email,i.e_contact)

    # e_dep=models.ForeignKey(Department,on_delete=models.CASCADE, related_name="dep")
    # data = Department.objects.all()
    # for i in data:
    #     print(i.d_name,i.d_hod,end=',')
    #     data1 = i.dep.all()
    #     for i in data1:
    #         print(i.e_name,i.e_email,i.e_contact)
    data = Department.objects.prefetch_related('dep')
    for i in data:
        print(i.d_name,i.d_hod,end=',')
        data1 = i.dep.all()
        for i in data1:
            print(i.e_name,i.e_email,i.e_contact)

def forword_data(req):
    # first method
    data = Student.objects.all()
    for i in data:
        print(i.name,i.courses.all())
    # second method
    data = Student.objects.prefetch_related('courses')
    for i in data:
        print(i.name,i.courses.all())