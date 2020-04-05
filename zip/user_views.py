from django.shortcuts import render
from .models import Car,User
from django.http import HttpResponse
from .forms import UserCreateForm

# Create your views here.

def user_search_view(request):
    form = request.GET
    user_search_query=form.get('user_search',None)
    users=User.objects.filter(first_name__contains=user_search_query)
    
    context={
        'users' : users
    }

    return render(request,'zip/user_detail.html', context )

def user_create_view(request):
    
    form = UserCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        form=UserCreateForm()
    
    else:
        print('form error')

    context={
        'form' : form
    }
    
    return render(request,'zip/user_create.html', context)

def user_view(request):
    users=User.objects.all()
    
    context={
        'users' : users
    }
    
    return render(request, 'zip/user_detail.html', context)

def user_search_form_view(request):
    return render(request, 'zip/user_search.html')

def user_login(request):
    return render(request, 'account/login.html')

def user_register(request):
    return render(request, 'account/register.html')