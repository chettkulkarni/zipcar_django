from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Car(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200)
    car_model=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.car_model

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)

    def __str__(self):
        return (self.first_name+self.last_name)