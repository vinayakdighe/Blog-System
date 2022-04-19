from turtle import home
from django.contrib import admin
from django.urls import path
from first import views


urlpatterns = [
   path('',views.index, name='home'),
   path('signup/',views.signup, name='signup'),
   path('login/',views.login, name='login'),
]