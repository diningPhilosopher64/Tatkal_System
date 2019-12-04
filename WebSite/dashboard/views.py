from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
)
import os
import json

#        -----------------View Functions-----------------------------



def dashboard(request):
    context = get_train_list()
    return render(request, 'dashboard/dashboard.html', context=context)



def user_bookings(request):
    user_id = request.user.id
    context = get_user_bookings(user_id)
    return render(request, 'dashboard/bookings.html', context= context)


def book_ticket(request, train_id, tickets_left):
    # Consume Ticket in /Trians/
    tickets_left -= 1
    if consume_ticket(train_id, tickets_left) == "Success":
        #Add ticket to user's booked tickets
        

        return dashboard(request)

       

    




    

#    --------------------- Helper Functions --------------------------

def get_train_list():
    content = json.loads(os.popen('curl bookingService:8000/trains/').read())       
    context = {
        "trains" : content,        
    }
    return context


def get_user_bookings(user_id):
    query = "curl bookingService:8000/bookings/"+ str(user_id)
    content = json.loads(os.popen(query).read())
    context = {
        "bookings" : content,        
    }
    return context


def consume_ticket(train_id, tickets_left):
    query = "curl bookingService:8000/trains/{}/{}".format(str(train_id), str(tickets_left))
    content = json.loads(os.popen(query).read())

    if content["status"] == "Success":
        return "Success"
    else:
        return "Failure"



