from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_view),
    path('home', views.home_view, name='home'),
    path('create_car', views.car_create_view),
]