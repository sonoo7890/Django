from django.db import models

# Create your models here.


from django.db import models
from cloudinary_storage.storage import VideoMediaCloudinaryStorage,RawMediaCloudinaryStorage,MediaCloudinaryStorage

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',storage=MediaCloudinaryStorage())
    audio = models.FileField(upload_to='audios/',storage=VideoMediaCloudinaryStorage())
    video = models.FileField(upload_to='videos/',storage=VideoMediaCloudinaryStorage())
    resume = models.FileField(upload_to='files/',storage=RawMediaCloudinaryStorage())