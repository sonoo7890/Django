from django.db import models

# Create your models here.
# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.IntegerField()
    # qualification = models.CharField(max_length=200)
    # gender  = models.CharField(max_length=10)
    # state = models.CharField(max_length=50) 
    # image = models.ImageField(upload_to='images/')
    # audio = models.FileField(upload_to='audios/')
    # video = models.FileField(upload_to='videos/')
    # document = models.FileField(upload_to='documents/')
    # password = models.CharField(max_length=20,null=True) # table pahle se created hai ab ek naya column add karne ke liye null =True use karna padta hai
    # profile_pic = models.ImageField(upload_to='profiles/'null=True,blank=True)
    # def __str__(self):
        # return str(self.contact)
        # return self.name
        # return f"{self.name} - {self.email}"
        # return f"{self.name}"
    
    # class Query(models.Model):
    #     name=models.CharField(max_length=20)
    #     email=models.CharField()
    #     query=models.CharField(max_length=200)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
