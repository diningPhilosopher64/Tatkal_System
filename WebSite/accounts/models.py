# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



# Create your models here.

# class Account(models.Model):
#     GENDER_CHOICES = [('M', 'MALE'), ('F', 'FEMALE')]    

#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     age = models.IntegerField(null = False, blank = False, validators = [MinValueValidator(1), MaxValueValidator(102)])
#     city = models.CharField(max_length = 50, blank = False, null = True)
#     gender = models.CharField(max_length = 2, choices= GENDER_CHOICES, default= "M", null = False, blank = False)

#     def __str__(self):
#         return self.name 


class AccountManager(BaseUserManager):
    def create_user(self, email, age, city, gender, password=None):
        """
        Creates and saves a User with the given email, age,city and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        elif not age:
            raise ValueError("User must have an age")
        elif not city:
            raise ValueError("User must have a city")
        elif not gender:
            raise ValueError("User must have a gender")

        user = self.model(
            email=self.normalize_email(email),
            age =age,
            city = city,
            gender = gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, age, city, gender, password):
        """
        Creates and saves a User with the given email, age,city and password.
        """
        user = self.create_user(
            email,
            age=age,
            city=city,
            gender=gender,
            password=password,            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    # email, is_active, is_admin are default from AbstractBaseUser we dont change that.
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    #Here we will add out custom fields which customizes the User model

    #first value in tuple is for User input and second value in tuple is what will be stored in db    
    GENDER_CHOICES = [('M', 'MALE'), ('F', 'FEMALE')]        
    age = models.IntegerField(null = False, blank = False, validators = [MinValueValidator(1), MaxValueValidator(102)])
    city = models.CharField(max_length = 50, blank = False, null = True)
    gender = models.CharField(max_length = 2, choices= GENDER_CHOICES, default= "M", null = False, blank = False)
    

    # Account needs an "AccountManager" to validate fields
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age', 'city', 'gender']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    