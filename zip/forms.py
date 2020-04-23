from django import forms
from .models import Car,User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields =[
            'owner',
            'car_model'
        ]

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'first_name',
            'last_name'
            # 'driving_license'
        ]




class UserForm(forms.ModelForm):


    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control text-box','title':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'user_login form-control text-box'}))

    class Meta():
        model = User
        fields = ('username','password')





# class CarSearchForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields =[
#             'car_model'
#         ]