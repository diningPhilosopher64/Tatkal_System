from django.db import models
from django.db import connection
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from Trains.models import Train

class Booking(models.Model):
    user_id = models.IntegerField(blank = True, null = True)
    train_id = models.ForeignKey(Train, on_delete= models.CASCADE, null = True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ('-date','user_id')

    def __str__(self):
        return str(self.user_id) + " booked train on " + self.date.strftime('%m/%d/%Y')


    def save(self, *args, **kwargs):
        if valid_user(self.user_id):
            super(Booking, self).save(*args, **kwargs)

        else:
            raise DoesNotExist

        
def valid_user(user_id):    
    try:
        with connection.cursor() as cursor:            
            row = cursor.execute("select * from accounts_account where id = "+ str(user_id) +";")   
            row = cursor.fetchone()

            if row:
                return True
            else:
                return False       
    except:
        return False
