from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('add', views.add),
    path('registration',views.registration),
    path('saveform1',views.saveform1),
    path('welcome',views.welcome),
    path('deletestudent/<int:id>',views.deletestudent),
    path('edit/<int:id>',views.edit),
    path('update_form',views.update_form),
]
