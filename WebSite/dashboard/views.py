from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
)
import os
import json

# Create your views here.


def get_train_list():
    content = json.loads(os.popen('curl bookingService:8000/trains/').read())       
    context = {
        "trains" : content,        
    }

    return content




def dashboard(request):
    context = get_train_list()
    print("\n\n user id is ", request.user.id, "\n\n")
    return render(request, 'dashboard/dashboard.html', context=context)


    