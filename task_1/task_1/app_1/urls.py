from django.urls import path
from app_1 import views

urlpatterns = [
    path("api_1/", views.insert_data, name="api"),
    path("api_dist/", views.district, name="api_dist")
]   