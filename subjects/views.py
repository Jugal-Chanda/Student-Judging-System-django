from django.shortcuts import render
from students.models import Student
from subjects.models import Subject
from django.http import JsonResponse


# Create your views here.

def create(request,id):
    data = {}
    student = Student.objects.get(pk=id)
    subject = Subject()
    subject.subject_name = request.POST.get('subject_name')
    subject.student = student
    subject.save()
    data['name'] = subject.subject_name
    data['id'] = subject.id
    return JsonResponse(data)
