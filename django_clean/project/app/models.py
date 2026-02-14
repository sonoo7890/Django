from django.db import models
from django.core.exceptions import ValidationError
#create your models here.
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
#Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15,null=True, blank=True)
    qualification = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    state =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    audio = models.FileField(upload_to='audio/',null=True, blank=True)
    video = models.FileField(upload_to='video/',null=True, blank=True)
    document = models.FileField(upload_to='document/',null=True, blank=True)
    password = models.CharField(max_length=20,null=True)#table me naya column add krne ke liye null=True likha

# def __str__(self):
#     return str(self.contact)
#     return self.name
#     return f"{self.name} - {self.email}"
#     return f"{self.name}"

def Emp1_contact(contact):
    if not(len(str(contact))==10 and  (contact.isdigit())):
       raise ValidationError("contact must be in 10 digits only")

class AddEmployee(models.Model):
    name = models.CharField(max_length=100,validators=[MinLengthValidator(3),])
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15,validators=[Emp1_contact])
    image = models.ImageField(upload_to='employee_profile/',null=True, blank=True)
    password = models.CharField(max_length=100,default='N/A')
    department = models.CharField(max_length=50,null=True)
    d_code = models.CharField(max_length=20,null=True)
    d_des = models.CharField(max_length=50,null=True)

    def clean(self):
        if not len(str(self.password))==4:
            raise ValidationError("Password must be 4 length")
    def save(self,*args,**kwargs):
        self.full_clean()
        super.save(*args,**kwargs)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Query(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    query =  models.CharField(max_length=200)
    subject = models.CharField(max_length=50) 
    status =  models.CharField(max_length=10,default='panding')
    solution = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

