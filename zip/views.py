from django.shortcuts import render
from .models import Car

# Create your views here.

def post_list(request):
    cars=Car.objects.all()
    return render(request, 'zip/post_list.html', {'cars': cars})
