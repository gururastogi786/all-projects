from tkinter import CASCADE
from django.db import models
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=100,blank="true")
    add = models.CharField(max_length=100,blank="true")
    email = models.CharField(max_length=100, blank="true")

    def __str__(self):
        return self.user_name


# class State(models.Model):
#     state_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.state_name


# class User(models.Model):
#     s_name = models.ForeignKey(State,on_delete=CASCADE)
#     name = models.CharField(max_length=100,blank="true")
#     state = models.CharField(max_length=100,blank="true")
#     email = models.CharField(max_length=100, blank="true")

#     def __str__(self):
#         return self.user_name


