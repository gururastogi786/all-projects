from django.contrib import admin
from app_1.models import User
from app_1.models import *
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["id","s_name"]

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["id","state_dist","d_name"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","state_user","dist_user","u_name","email","password","avatar"]

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["id","sub_user","sub_name"]

@admin.register(Free)
class FreeAdmin(admin.ModelAdmin):
    list_display = ["id","f_user","f_name"]
