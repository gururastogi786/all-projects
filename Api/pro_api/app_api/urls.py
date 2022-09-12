from django.contrib import admin
from django.urls import path,include
from app_api import views

urlpatterns = [
    path("",views.index,name='index'),
    path("api/", views.Er_Anmol_Rastogi, name="api"),
    path("savedept/", views.add_dept, name="savedept"),
    path("add_emp/", views.add_emp, name="add_emp"),
    path("delete_adhar", views.delete_adhar, name="delete_adhar"),
    path("update_emp", views.update_emp, name="update_emp")
]
