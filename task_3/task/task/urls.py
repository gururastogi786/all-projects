from django.contrib import admin
from django.urls import path
from app_3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.User),
    

]
