from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
    ListView,
)
import os
import json
from django.core import serializers
from django.http import JsonResponse

#        -----------------View Functions-----------------------------



def dashboard(request):
    context = get_train_list()
    return render(request, 'dashboard/dashboard.html', context=context)



def user_bookings(request):
    user_id = request.user.id
    context = get_user_bookings(user_id)
    return render(request, 'dashboard/bookings.html', context= context)


def book_ticket(request, train_id, tickets_left):
    tickets_left -= 1
    data = {
        "ticket_count":-1
    }

    if consume_ticket(train_id, tickets_left) == "Success":
        if add_ticket(request.user.id, train_id) == "Success":
            data["ticket_count"] = tickets_left                     
            return JsonResponse(data)

   
    return  JsonResponse(data)
    

       

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

def add_ticket(user_id, train_id):
    query = "curl bookingService:8000/bookings/{}/{}".format(str(user_id), str(train_id))
    content = json.loads(os.popen(query).read())

    if content["status"] == "Success":
        return "Success"
    else:
        return "Failure"



