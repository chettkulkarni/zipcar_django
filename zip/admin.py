from django.contrib import admin
from .models import Car,User,Transactions

admin.site.site_header = 'Four_Real_ZipCar'

# Register your models here.

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Transactions)

