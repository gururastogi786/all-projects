from csv import list_dialects
from django.contrib import admin
from app_api.models import Adhar, Department, Employee, Product 
from app_api.models import models

# Register your models here.
admin.site.register(Employee)
admin.site.register(Adhar)



admin.site.register(Department)
admin.site.register(Product)

class AdharAdmin(admin.ModelAdmin):
    list_display=["Adhar_number"]