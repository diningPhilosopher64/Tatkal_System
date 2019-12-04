from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from datetime import datetime


from .models import *
from Trains.models import *
from .serializers import *


class BookingList(APIView):
    def get(self, request, *args, **kwargs):        
        user_id = kwargs.get('user_id', '-1')
        user_bookings = Booking.objects.filter(user_id = user_id)
        user_bookings_serializer = BookingSerializer(user_bookings, many = True)
        return Response({"user_bookings" : user_bookings_serializer.data})   


class AddBooking(APIView):
    def get(self, request, *args, **kwargs):
        user_id = int(kwargs.get('user_id', '-1'))
        train_id = int(kwargs.get('train_id', '-1'))

        context = {
            "status":"Failure"
        }

        try:
            train = Train.objects.filter(id = train_id).get()
            booking = Booking(user_id = user_id, train_id = train, date = datetime.now())
            booking.save()            
            context["status"] = "Success"

        except:
            pass


        return Response(context)

class AllBookings(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    name = 'all-bookings-list'


        



