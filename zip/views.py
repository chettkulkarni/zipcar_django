from django.shortcuts import render
from .models import Car,User
from django.http import HttpResponse

from .forms import CarCreateForm,CarSearchForm

# Create your views here.

def default_view(request):
      return render(request, 'base.html')