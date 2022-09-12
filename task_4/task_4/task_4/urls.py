# ------------------------------------------------

# from django.contrib import admin
# from django.urls import path,include
# from app_4 import views

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('State',views.StateViewSet, basename="State")
# router.register('District',views.DistrictViewSet,basename='District')
# router.register('User',views.UserViewSet, basename="User")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include(router.urls)),
#     path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    

# ]

# -------------------------------------------------------------
from django.contrib import admin
from django.urls import path
from app_4.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("state/", ListState.as_view()),
    path("district/", Districtapi.as_view()),
    path("user/", Userapi.as_view()),
    path("show/", Showuserapi.as_view()),
]