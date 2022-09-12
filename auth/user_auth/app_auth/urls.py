import imp
from django.contrib import admin
from django.urls import path,include
from app_auth import views

urlpatterns = [
    path('', views.index, name="app_auth"),
    path('login/',views.loginuser, name="login"),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
]
