from django.db import models
from django.contrib import admin
from app_3.models import *
# Create your models here.
# ------------------------------------------user detail--------------------------------

# class State(models.Model):
#     state_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.state_name

# class District(models.Model):
#     district = models.CharField(max_length=100)

#     def __str__(self):
#         return self.district

# class User(models.Model):
#     user_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     district =models.ForeignKey(District, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user_name


# --------------------------------------second------------------------------------

class User(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

