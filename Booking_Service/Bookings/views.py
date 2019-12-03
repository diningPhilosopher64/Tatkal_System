from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import *
from .serializers import *


class BookingList(APIView):
    def get(self, request, *args, **kwargs):        
        user_id = kwargs.get('user_id', '-1')
        user_bookings = Booking.objects.filter(user_id = user_id)
        user_bookings_serializer = BookingSerializer(user_bookings, many = True)
        return Response({"user_bookings" : user_bookings_serializer.data})   
    

# class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookingSerializer
#     name = 'booking-detail'

#     def get_queryset(self):        
#         user = self.request.user
#         return Booking.objects.filter(user_id=user.id)


class AllBookings(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    name = 'all-bookings-list'


        



