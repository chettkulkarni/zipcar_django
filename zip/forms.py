from django import forms
from .models import Car,User

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
        ]

# class CarSearchForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields =[
#             'car_model'
#         ]  