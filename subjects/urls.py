from django.urls import path,include
from subjects import views

urlpatterns = [
    path('create/<int:id>',views.create,name='subject.create'),
]
