from django.db import models

# Create your models here.
class student(models.Model):
    # id= models.IntegerField(max_length=50)  this will create automatically
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100,default='pune')
