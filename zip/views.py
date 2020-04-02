from django.shortcuts import render
from .models import Car,User
from django.http import HttpResponse

from .forms import CarForm

# Create your views here.

def car_create_view(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save
    
    context={
        'form' : form
    }
    return render(request,'zip/car_create.html', context)

def home_view(*args,**kwargs):
    return HttpResponse("<h1> Hello World!1 </h1>")

def car_view(request):
    
    # context={}
    cars=Car.objects.all()
    return render(request, 'zip/car_detail.html', {'cars': cars})
