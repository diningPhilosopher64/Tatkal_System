from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, get_user






def register_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        print("\n\n\n  ffff", get_user(request), "\n")

        if user_form.is_valid():            
            user_form.save()
            user = get_user(request)           
            account_form = AccountCreationForm(data = request.POST, instance= user.account)
            account_form.save()

        return render(request, 'accounts/login.html')

    else:
        user_form = UserCreationForm()
        account_form = AccountCreationForm()

        return render(request, 'accounts/register.html', {
            'user_form': user_form,
            'account_form': account_form
        })


def login_user(request):  
    if request.method == 'POST':        
        login_form = AuthenticationForm(data = request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            print("\n \n \n logged user ", user)
            login(request, user)
            # return render(request, "dashboard/dashboard.html")
            return redirect("dashboard:dashboard")

    else:
        login_form = AuthenticationForm()
        return render(request, "accounts/login.html", {
            "user_form": login_form
        })



def logout_user(request):   
    logout(request)
    return redirect("accounts:login")

    

