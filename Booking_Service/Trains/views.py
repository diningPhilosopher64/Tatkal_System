from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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




class ConsumeTicket(APIView):
    def get(self, request, *args, **kwargs):
        train_id = kwargs.get('train_id')
        tickets_left = kwargs.get('tickets_left')

        context = {
            "status":"Failure"
        }
        
        train = Train.objects.filter(id= train_id).get()
        train.tickets_left = tickets_left

        try:
            train.save()
            context["status"] = "Success"
        
        except:
            pass
        
        return Response(context)


class BookTrain(APIView):
    def post(self, request, *args, **kwargs):        
        train_id = kwargs.get('train_id', -1)
        train = Train.objects.filter(id = train_id)
        train.tickets_left -= 1
        train.save()
        train_serializer = TrainSerializer(train)
        return Response({""})

