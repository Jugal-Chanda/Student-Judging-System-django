from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='student_image')
    fullname = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique = True,max_length=40)
