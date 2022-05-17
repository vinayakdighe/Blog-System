from turtle import home
from django.contrib import admin
from django.urls import path
from first import views


urlpatterns = [
   path('',views.index, name='home'),
   path('signup/',views.signup, name='signup'),
   path('signup/register', views.register, name='register'),
   #changed by samruddhi
   path('saveRegister/',views.saveRegister,name='saveRegister'),
   #upto these
   path('login/',views.login, name='login'),
   path('online marketing/',views.writting,name='online marketing'),
   path('social media/',views.writting,name='social media'),
   path('technology/',views.technology, name= 'technology'),
   path('writting/',views.writting,name='writing'),
   
]