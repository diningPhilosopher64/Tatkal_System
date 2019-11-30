from django.shortcuts import render
from accounts.models import Account
from django.views.generic import (
    DetailView,
    ListView,
)
import os
import json




# Create your views here.



def train_list(request):
    content = json.loads(os.popen('curl bookingService:8000/trains/').read())       
    context = {
        "trains" : content
    }

    return render(request, 'dashboard/dashboard.html', context=context)


def booking_list(request):
    #curl -X GET bookingService:8000/bookings?user_id=1
    print("\n\n ID is" , request.user.id, "\n\n")
    # query = "curl bookingService:8000/bookings/?user_id="+ str(request.user.id)
    query = "curl bookingService:8000/bookings/"+ str(request.user.id)

    print("\n\n\n  ", query, "\n\n\n" )
    print("\n\n content is : \n", os.popen(query).read(), "\n\n\n")
    content = json.loads(os.popen(query).read())
    # content = os.popen(query).read()


    context = {
        "bookings" : content
    }
    return render(request, "dashboard/bookings.html", context= context)





