from django.db import models

# Create your models here.

class contactUs(models.Model):
      
      name = models.CharField(max_length=22, default=None)
      number = models.IntegerField(default=None)
      address = models.CharField(max_length=22, default=None)
      state = models.CharField(max_length=22, default=None)
      district = models.CharField(max_length=22, default=None)
      village = models.CharField(max_length=22, default=None)
      Password = models.CharField(max_length=22, default=None)
      c_pass = models.CharField(max_length=22, default=None)


      def __str__(self):
            return self.name

