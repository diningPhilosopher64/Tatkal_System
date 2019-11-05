from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *

class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    name = 'bookings-list'

    def get_queryset(self):        
        user = self.request.user
        return Booking.objects.filter(user_id=user.id)
    

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    name = 'booking-detail'

    def get_queryset(self):        
        user = self.request.user
        return Booking.objects.filter(user_id=user.id)


class AllBookings(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    name = 'all-bookings-list'


