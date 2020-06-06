from django.db import models
from students.models import Student
# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=40)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
