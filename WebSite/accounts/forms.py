from django import forms
from django.contrib.auth import authenticate
from .models import *

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('city', 'gender')

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username and password:
            user = authenticate(username = username, password = password)
            
            if not user:
                raise forms.ValidationError("User doesnt exist")
            
            if not user.check_password(password):
                raise forms.ValidationError("Wrong Password")

            if not user.is_active:
                raise forms.ValidationError("User inactive")

        return super(UserLoginForm, self).clean(*args, **kwargs)



