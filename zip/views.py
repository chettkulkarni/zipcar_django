from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from . import user_views
from .models import Car, User
from django.http import HttpResponse, HttpResponseRedirect
from . import urls

# from .forms import CarCreateForm
# CarSearchForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def default_view(request):
    return render(request, 'base.html')


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect(user_views.user_login())


def user_login1(request):
    print(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(request)
        if user:
            if user.is_active:
                login(request, user)
                print('here')
                return render(request, 'dashboards/userDash.html' , {})

            else:
                return HttpResponse("Your account was inactive.")
        else:
            return render(request, 'registration/login.html', {})

    return render(request, 'registration/login.html', {})
