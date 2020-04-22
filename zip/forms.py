from django import forms
from .models import Car,User
from django.urls import reverse_lazy

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
            'last_name',
            'driving_license'
        ]

# class CarSearchForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields =[
#             'car_model'
#         ]  