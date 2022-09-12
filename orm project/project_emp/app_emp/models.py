from django.db import models

# Create your models here.
class Departmant(models.Model):
    dept_id = models.IntegerField()
    dept_Name = models.CharField(max_length=122)

    def __str__(self):
        return str(self.dept_Name)

class Adhar(models.Model):
    adhar_id = models.IntegerField()

    def __str__(self):
        return str(self.adhar_id)

class Employee(models.Model):
    dept = models.ForeignKey(Departmant, on_delete=models.CASCADE)
    adhar = models.OneToOneField(Adhar, on_delete=models.CASCADE)
    emp_Name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    joining_Date = models.DateField()

    def __str__(self):
        return self.emp_Name

class Product(models.Model):
    employee = models.ManyToManyField(Employee)
    product_Name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.product_Name)  
    





