from django.db import models

# Create your models here.

class My_car(models.Model):
    Number_of_brakes = models.CharField(max_length=200)