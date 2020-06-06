from django.db import models
from subjects.models import Subject
# Create your models here.

class Chapter(models.Model):
    chapter_title = models.CharField(max_length=20)
    chapter_name = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    description = models.TextField(null = True)

    def __str__(self):
        return self.chapter_title
