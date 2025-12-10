from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.formsave),
    path('formcheck',views.formcheck),
    path('signin',views.signin),
    path('signcheck',views.signcheck),
    path('dashboard',views.dashboard),
    path('signout',views.signout),
    path('resetpassword',views.resetpassword),
    path('reset',views.reset),
]
