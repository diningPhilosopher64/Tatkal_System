from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    name = 'booking-list'

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    name = 'booking-detail'