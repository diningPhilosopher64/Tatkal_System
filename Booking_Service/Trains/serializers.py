from .models import *
from rest_framework import serializers

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = (
            'id',
            'name',
            'departure_station',
            'destination_station',
            'tickets_left'
        )
