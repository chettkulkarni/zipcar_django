from django.conf.urls import url
from django.urls import path
from . import car_views, user_views
from . import views

urlpatterns = [
    path('', car_views.default_view),

    # car routings
    path('cars/', car_views.car_view),
    path('car_create', car_views.car_create_view),
    path('car_search_form', car_views.car_search_form_view),
    path('car_search', car_views.car_search_view),
    path('car_request/<car>/', car_views.car_request_view),

    # user routings
    # path('users', user_views.user_view),
    # path('user_create', user_views.user_create_view),
    # path('user_search_form', user_views.user_search_form_view),
    # path('user_search', user_views.user_search_view),
    # path('user_login', user_views.user_login),
    # path('user_register', user_views.user_register),
    # path('user_logout', views.logout_request, name = 'logout'),
    # path('user_login1', views.user_login1),


    # dash boards
    path('user_dash', user_views.user_dash),
    path('admin_dash', user_views.admin_dash),


    path('register',views.register),
    path('user_login',views.user_login),
    path('', views.index),
    url('^$',views.index,name='index'),
    url('^special/',views.special,name='special'),
    url('^logout/$', views.logout_request, name='logout'),
    url('^register/$',views.register,name='register'),
    url('^user_login/$',views.user_login,name='user_login')
]
