from django.contrib import admin
from app_3.models import *
# Register your models here.
# ------------------------------user detail--------------
# @admin.register(State)
# class StateAdmin(admin.ModelAdmin):
#     list_display = ["id","state_name"]


# @admin.register(District)
# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ["id","district"]

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["id","user_name","email","state","district"]

# -------------------------second---------------------

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","user_name","email","state","district"]