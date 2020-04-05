from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Car(models.Model):
    owner = models.CharField(max_length=200)
    car_model=models.CharField(max_length=200)
   
    def __str__(self):
        return self.car_model

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)

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