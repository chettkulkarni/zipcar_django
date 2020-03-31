from django.shortcuts import render
from .models import Car,User

# Create your views here.

def post_list(request):
    cars=Car.objects.all()
    users=User.objects.all()
    return render(request, 'zip/post_list.html', {'cars': cars,'users':users})
