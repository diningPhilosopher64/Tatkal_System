from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

class Account(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,related_name='account')
    GENDER_CHOICES = [('M', 'MALE'), ('F', 'FEMALE')]        
    age = models.IntegerField(null = True, blank = True, validators = [MinValueValidator(1), MaxValueValidator(102)])
    city = models.CharField(max_length = 50, blank = True, null = True)
    gender = models.CharField(max_length = 2, choices= GENDER_CHOICES, default= "M", null = True, blank = True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()