from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *
# Create your views here.

class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name = 'train-list'

class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    name='train-detail'
