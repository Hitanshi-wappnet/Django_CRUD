from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField(max_length=100)
    salary = models.CharField(max_length=10)

