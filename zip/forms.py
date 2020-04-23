from django import forms
from .models import Car,Person
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
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Person
        fields =[
            'first_name',
            'last_name',
            'username',
            'driving_licence',
            'password'
        ]




class UserLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control text-box','title':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'user_login form-control text-box'}))
    class Meta():
        model = User
        fields = ('email','password')

# class UserRegisterForm(forms.ModelForm):
#     First_Name =
#     username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control text-box','title':'username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'user_login form-control text-box'}))
#     class Meta():
#         model = User
#         fields = ('username','password')





# class CarSearchForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields =[
#             'car_model'
#         ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Person
         fields =[
            'first_name',
            'last_name',
            'driving_licence',
        ]