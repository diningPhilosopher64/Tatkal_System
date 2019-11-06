from .models import Account
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

from django.contrib.auth import authenticate, login


def user_base(request):
    # if this is a POST request we need to process the form data
    template = 'accounts/base.html'
    return render(request, template,{})

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'accounts/register.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if Account.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:

                accnt = Account.objects.create_user(email=form.cleaned_data['email'],password=form.cleaned_data['password'],age=form.cleaned_data['age'],
                city=form.cleaned_data['city'],gender=form.cleaned_data['gender'])
                accnt.save()
               
                # Login the user
                #login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/accounts/login')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['email']
        password = request.POST['password']
        # Check username and password combination if correct
        accnt = authenticate(username=username, password=password)
        if accnt is not None:
            # Save session as cookie to login the user
            login(request, accnt)
            # Success, now let's login the user.
            obj=Account.objects.get(email=username)
            return render(request, 'accounts/dashboard.html',{'object':obj})
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'accounts/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'accounts/login.html')