from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    owner = models.CharField(max_length=200)
    car_model=models.CharField(max_length=200)
   
    def __str__(self):
        return self.car_model

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username =models.CharField(max_length=200)
    first_name =models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    driving_licence =models.CharField(max_length=200)
    def __str__(self):
        return (self.first_name+self.last_name)


STATUS_CHOICES = [
    ("Requested", "Requested"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected"),
]

class Transactions(models.Model):
    user = models.CharField(max_length=200)
    car =models.CharField(max_length=200)
    status=models.CharField(max_length=200, choices=STATUS_CHOICES)
    def __str__(self):
        return (self.user+self.car+self.status)