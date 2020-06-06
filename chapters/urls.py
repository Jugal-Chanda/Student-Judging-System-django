from django.urls import path,include
from chapters import views

urlpatterns = [
    path('create/<int:id>',views.create,name="chapters.create"),
    path('index/<int:id>',views.index,name="chapters.index"),
    path('addrating/',views.addrating,name="chapters.addrating"),
]
