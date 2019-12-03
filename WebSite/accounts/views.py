from django.shortcuts import render
from .forms import *




def register_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance= request.user)
        account_form = AccountCreationForm(request.POST, instance= request.user.account)
        if user_form.is_valid() and account_form.is_valid():
            print("\n\n\n forms valid", account_form)
            user_form.save()
            account_form.save()
            return render(request, "accounts/login.html")
    else:
        user_form = UserCreationForm(instance=request.user)
        account_form = AccountCreationForm(instance=request.user.account)

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'account_form': account_form
    })


def login_user(request):
    if request.method == "POST":
        user_form = UserLoginForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return render(request, "dashboard/dashboard.html")
    
    else:
        user_form = UserLoginForm(instance=request.user)

    return render(request, 'accounts/login.html', {
        'user_form': user_form,        
    })
    

