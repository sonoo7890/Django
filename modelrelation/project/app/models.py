from django.db import models

# Create your models here.
class Aadhar(models.Model):
    adhar_no=models.CharField(max_length=12,unique=True)
    create_at=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return  str(self.adhar_no)

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    adhar_no=models.OneToOneField(Aadhar,on_delete=models.PROTECT) # related_name used only for reverse access.
    def __str__(self):
        return  str(self.name)
class Department(models.Model):
    d_name = models.CharField(max_length=20)
    d_hod = models.CharField(max_length=20)
    def __str__(self):
        return  str(self.d_name)
    
class Employee(models.Model):
    e_name=models.CharField(max_length=20)
    e_email=models.EmailField()
    e_contact=models.IntegerField()
    e_dep=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='dep')
    def __str__(self):
        return  str(self.e_name)
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class Student1(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)   # M2M relation
    def __str__(self):
        return self.name