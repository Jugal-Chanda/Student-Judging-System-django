from django.urls import path,include
from students import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('addstudents/',views.addstudents,name='ajax.addstudents'),
    path('updateprofileimage/<int:id>',views.updateProfileImage,name='ajax.updateimage'),
    path('updateprofileinfo/<int:id>',views.updateprofileinfo,name='ajax.updateinfo'),

]
