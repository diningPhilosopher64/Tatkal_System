from django.shortcuts import render
from accounts.models import Account
from django.views.generic import (
    DetailView,
    ListView,
)
import os
import json

# Create your views here.



def trainList(request):
    
       
    content = json.loads(os.popen('curl bookingService:8000/trains/').read())   
    
    context = {
        "trains" : content
    }

    return render(request, 'dashboard/dashboard.html', context=context)


 



