from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        

class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ('age', 'city', 'gender')


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

