from .models import Train
from rest_framework import serializers

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = (
            'url',
            'pk',
            'name',
            'departure_station',
            'destination_station',
            'tickets_left'
        )





