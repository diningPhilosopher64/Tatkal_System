from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.db import connection

# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=100, null = True, blank= False)
    train_number = models.IntegerField(null= False, blank= False, default= 0)
    departure_station = models.CharField(max_length=100, null = True, blank= False)
    destination_station = models.CharField(max_length=100, null = True, blank= False)
    tickets_left = models.IntegerField(null = False, blank = False,default = 1000, validators = [MinValueValidator(1), MaxValueValidator(1000)])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

