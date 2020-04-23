from django.contrib import admin
from .models import Car,Person,Transactions

admin.site.site_header = 'Four_Real_ZipCar'

# Register your models here.

admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Transactions)

