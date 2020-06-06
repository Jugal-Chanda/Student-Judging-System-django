from django.shortcuts import render
from .forms import add_student_form
from django.http import JsonResponse
from .models import Student
from django.template import Context, Template

# Create your views here.

def home(request):
    context = {}
    studets = Student.objects.all()
    context['studets'] = studets
    return render(request, 'home.html',context)

def profile(request,id):
    context = {}
    student = Student.objects.get(pk=id)
    context['subjects'] = student.subject_set.all()
    context['student'] = student
    return render(request, 'profile.html',context)

def addstudents(request):
    data = {}
    if request.POST:
        form = add_student_form(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            data['check'] = True
            data['fullname'] = student.fullname
            data['phone'] = student.phone
            data['email'] = student.email
            data['image'] = student.image.url
            data['id'] = student.id
        else:
            data['check'] = False
            data['error'] = form.errors.as_json()
    return JsonResponse(data)

def updateProfileImage(request,id):
    data = {}
    student = Student.objects.get(pk=id)
    student.image = request.FILES.get('image')
    student.save();
    data['check'] = True
    data['img'] = student.image.url
    return JsonResponse(data)

def updateprofileinfo(request,id):
    data = {}
    student = Student.objects.get(pk=id)
    student.fullname = data['fullname'] = request.POST.get('fullname')
    student.email = data['email']= request.POST.get('email')
    student.phone = data['phone'] = request.POST.get('phone')
    student.save()
    return JsonResponse(data)
