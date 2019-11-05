from .models import *
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


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    train_id = TrainSerializer()

    class Meta:
        model = Booking
        fields = (
            'url',
            'pk',
            'train_id',
            'date',
            'user_id',
        )





