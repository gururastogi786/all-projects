from pyexpat import model
from django.db import models

# Create your models here.

class State(models.Model):
    s_name=models.CharField(max_length=100)

    def __str__(self):
        return self.s_name

class District(models.Model):
    state_dist = models.ForeignKey(State,on_delete=models.CASCADE)
    d_name=models.CharField(max_length=100)

    def __str__(self):
        return self.d_name

class User(models.Model):
    state_user = models.ForeignKey(State, on_delete=models.CASCADE)
    dist_user = models.ForeignKey(District, on_delete=models.CASCADE)
    u_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    avatar=models.ImageField()

    def __str__(self):
        return self.u_name


class Subscription(models.Model):
    sub_user = models.OneToOneField(User,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name

class Free(models.Model):
    f_user = models.OneToOneField(User,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)

    def __str__(self):
        return self.f_name
