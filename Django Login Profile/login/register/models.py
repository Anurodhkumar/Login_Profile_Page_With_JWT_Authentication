from django.db import models

# Create your models here.

class CreateUser(models.Model):
    fname=models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email=models.EmailField(max_length=128)
    password=models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    address=models.CharField(max_length=128)