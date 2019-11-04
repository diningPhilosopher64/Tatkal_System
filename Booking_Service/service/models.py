from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=100)
    departure_station = models.CharField(max_length=100)
    destination_station = models.CharField(max_length=100)
    tickets_left = models.IntegerField(null = False, blank = False,default = 1000, validators = [MinValueValidator(1), MaxValueValidator(1000)])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user_id = models.IntegerField(blank = True, null = True)
    train_id = models.ForeignKey(Train, on_delete= models.CASCADE, null = True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ('-date','user_id')

    def __str__(self):
        return str(self.user_id) + " booked train on " + self.date.strftime('%m/%d/%Y')
