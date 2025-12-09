from django.db import models
from setuptools.command.upload import upload


# Create your models here.
class student(models.Model):
    # id= models.IntegerField(max_length=50)  this will create automatically
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100,default='pune')

class employee(models.Model):
    name = models.CharField(max_length= 100)
    photos = models.FileField(upload_to ='images')

class person(models.Model):
    fullname = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)
    city = models.CharField(max_length=100)