from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def landing(req):
    return render(req,'landing.html')


def register(req):
    # print(req.method) 
    # print(req.POST)
    # print(req.FILES)

    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        q = req.POST.getlist('qualification[]')
        g = req.POST.get('gender')
        s = req.POST.get('state')
        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('document')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        print(n,e,c,q,g,s,i,a,v,d,p,cp,sep='\n')

        user = Employee.objects.filter(email=e)
        if user:

            req.session['xyz']=f"{e} Email already exist"
            return redirect('register')
        else:

            if p == cp:
                Employee.objects.create(name=n,email=e,contact=c,qualification=','.join(q),
                                        gender=g,state=s,image=i,audio=a,video=v,document=d,password=p)
                req.session['pqr']="Registarion done"
                # return HttpResponse("Registered Successfully")
                return redirect('login')
            else:
                req.session['xyz']="Password and conform password not matched"
                return redirect('register') 

    else:
        # msg =req.session['xyz']
        msg = req.session.get('xyz','')
        signup=req.session.get('signup','')
        # del req.session['xyz']
        req.session.flush()
        return render(req,'register.html',{'msg':msg})

def show_data(req): 

    #Query that work on single object..............

    # data=Employee.objects.get(id=6)
    data = Employee.objects.all()
    # print(data.name,data.email,data.contact)
    # return render(req,'show_data.html',{'data':data})
    # data=Employee.objects.first()
    # data=Employee.objects.last()
    # data=Employee.objects.latest('name')
    # data=Employee.objects.earliest('name')
    # data=Employee.objects.create()
    # print(data.name,data.email,data.contact)
    return render(req,'show_data.html',{'data':data})

    # data = Employee.objects.all()
    # print(data.name,data.email,data.contect)



    # data = Employee.objects.all()
    # print(data)
    # for i in data:
    #     print(i.name,i.email,i.contact)
    # return render(req,'show_data.html',{'data':data})


    # data = Employee.objects.filter(gender="female")
    # data = Employee.objects.exclude(gender="female")
    # data = Employee.objects.order_by('gender')
    # data = Employee.objects.order_by('name')   # (assending order)
    # data = Employee.objects.order_by('-name')  #(decending order )

    
    
    # return render(req,'show_data.html',{'data':data})
def login(req):
    
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')

        user = Employee.objects.filter(email=e).first()

        # ❌ user not found
        if not user:
            return render(req, 'login.html', {
                'pqr': f'{e} is not registered'
            })

        # ❌ password wrong
        if p != user.password:
            return render(req, 'login.html', {
                'pqr': 'Wrong password'
            })

        # ✅ SUCCESS LOGIN
        req.session['user_id'] = user.id
        return redirect('admin_dashboard')   # 🔥 SIDHE ADMIN DASHBOARD

    return render(req, 'login.html')

    #     p=req.POST.get('password')
    #     user=Employee.objects.filter(email=e)
    #     if not user:
    #         req.session['signup']=f'{e} is not register'
    #         return redirect('admin_dashboard')
    #         if user:
    #            login(req, user)
    #         return redirect('dashboard') 
    #     else:
    #         user_data=Employee.objects.get(email=e)
    #         sp=user_data.password
    #         if p==sp:
    #             req.session['user_id']=user_data.id
    #             return redirect('dashboard')

    # pqr=req.session.get('pqr')
    # # req.session.flush()
    # return render(req,'login.html',{'pqr':pqr})


def dashboard(req):
    # if req.session['user_id']:
        #   id=req.session['user_id']
   
        #   userdata=Employee.objects.get(id=id)
        #   return render(req,'dashboard.html',{'data':userdata})
    # else:
        return render(req,'dashboard.html')
        # return redirect('login')


def admin_dashboard(req):
    # users = Employee.objects.all()

    # return render(req, 'admin_dashboard.html', {
    #     'users': users
    # })
    
    # 🔐 login protection
    if not req.session.get('user_id'):
        return redirect('login')

    # users = Employee.objects.all()
    return render(req, 'admin_dashboard.html', {'users': users})

def admin_dashboard(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # profile = request.FILES.get('profile_pic')

        if password == cpassword:
            Employee.objects.create(
                name=name,
                email=email,
                contact=contact,
                password=password,
                # profile_pic=profile
            )

    users = Employee.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})


def add_employee(req):
    if req.method == 'POST':
       
        name = req.POST.get('name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        password = req.POST.get('password')
        department = req.POST.get('department')
        # profile = req.FILES.get('profile')

        Employee.objects.create(
            name=name,
            email=email,
            contact=contact,
            password=password,
            department=department,
            # profile_pic=profile
        )
        messages.success(req, "Employee added successfully ✅")
        return redirect('admin_dashboard')
    return render(req, 'admin_dashboard')

def show_employee(request):
    employees = Employee.objects.all().order_by('id')  # latest upar
    return render(request, 'show_all_employee.html', {
        'employees': employees
    })

def logout(req):
    if req.session.get('user_id',None):
        req.session.flush()
        return redirect('login')
    return redirect('login')
