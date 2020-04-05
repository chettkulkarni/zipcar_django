from django.shortcuts import render
from .models import Car,User,Transactions
from django.http import HttpResponse
from .forms import CarCreateForm

# Create your views here.

def car_search_view(request):
    form = request.GET
    car_search_query=form.get('car_model_search',None)
    cars=Car.objects.filter(car_model__contains=car_search_query)

    context={
        'cars' : cars
    }
    return render(request,'zip/car_detail.html', context )

def car_create_view(request):
    
    form = CarCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        form=CarCreateForm()
    
    else:
        print('form error')

    context={
        'form' : form
    }
    
    return render(request,'zip/car_create.html', context)

def car_search_form_view(request):
    return render(request, 'zip/car_search.html')

def default_view(request):
      return render(request, 'base.html')

def car_view(request):
    # context={}
    cars=Car.objects.all()
    context={
        'cars' : cars
    }
    return render(request, 'zip/car_detail.html', context)

def car_request_view(request,car):
    
    # User.objects.filer to see if user is legit or not
    # See if car is available or not
    # if user exists and car exists register it
    user='requested_user_id_comes_here'
    status='Pending'
    transaction=Transactions(user=user,car=car,status=status)
    transaction.save()
    return render(request, 'zip/car_search.html')
