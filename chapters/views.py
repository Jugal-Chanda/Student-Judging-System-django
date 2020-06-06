from django.shortcuts import render
from subjects.models import Subject
from chapters.models import Chapter
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Avg
# Create your views here.
def create(request,id):
    data = {}
    subject = Subject.objects.get(pk=id)
    chapter  = Chapter()
    chapter.chapter_title = request.POST.get('chapter_title')
    chapter.chapter_name = request.POST.get('chapter_name')
    chapter.subject = subject
    chapter.save()
    data['chapter'] = serializers.serialize('json', Chapter.objects.filter(pk=chapter.id))
    return JsonResponse(data)

def index(request,id):
    data ={}
    subject = Subject.objects.get(pk=id)
    chapters  = subject.chapter_set.all()
    data['chapters'] = serializers.serialize('json', chapters)
    return JsonResponse(data)

def addrating(request):
    data = {}
    chapter = Chapter.objects.get(pk=request.POST.get('chapter_id'))
    chapter.rating = request.POST.get('rating')
    chapter.chapter = request.POST.get('description')
    chapter.save()
    subject = chapter.subject
    check = (Chapter.objects.filter(subject=subject).aggregate( aver = Avg('rating')))
    subject.rating = check['aver']
    subject.save()
    student = subject.student
    check = Subject.objects.filter(student=student).aggregate( aver = Avg('rating'))
    student.rating = check['aver']
    student.save()
    return JsonResponse(data)
