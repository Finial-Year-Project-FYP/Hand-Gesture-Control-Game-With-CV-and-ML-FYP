from django.db import models

# Create your models here.

class My_car(models.Model):
    name = models.CharField(max_length=200, default=0)
    roll_no = models.CharField(max_length=200, default=0)
    Number_of_brakes = models.CharField(max_length=200)