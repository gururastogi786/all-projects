from django.contrib import admin
from .models import State ,District, User
# Register your models here.

# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(User)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id',"state_name"]

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id',"s_name","dict_name"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","user_name","email","password","state","district"]