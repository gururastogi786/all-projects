from django.db import models

# Create your models here.

# -------------------------------------------------------------------
class State(models.Model):
    state_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.state_name

class District(models.Model):
    s_name = models.ForeignKey(State, default=True, on_delete=models.CASCADE,related_name="state_disct")
    dict_name = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.dict_name
    

class User(models.Model):
    user_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default=True,related_name="obj")
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
  


# -----------------------------------------------sir code------------------------
# class State(models.Model):
#     name = models.CharField(max_length=200, null=False, blank=False)
#     def __str__(self):
#         return self.name
# class District(models.Model):
    # state = models.ForeignKey(State, default=True, on_delete=models.CASCADE, related_name="state_disct")
    # name = models.CharField(max_length=200, null=False, blank=False)
    # def __str__(self):
    #     return self.name

# class UserPro(models.Model):
#     name = models.CharField(max_length=200, null=False, blank=False)
#     rollno = models.CharField(max_length=200, null=False, blank=False)
#     state = models.ForeignKey(State, default=True, on_delete=models.CASCADE, related_name="state_obj")
#     district = models.ForeignKey(District, default=True, on_delete=models.CASCADE, related_name="district")

#     def __str__(self):
#         return self.name

