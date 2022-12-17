from django.db import models

# Create your models here.


class My_car(models.Model):
    Number_of_brakes = models.CharField(max_length=200, default=None)
    player_name = models.CharField(max_length=200, default=None)
    player_ID = models.CharField(max_length=200, default=0)
    RANK = models.CharField(max_length=200, default=None)
