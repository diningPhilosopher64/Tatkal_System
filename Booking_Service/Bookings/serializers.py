from .models import *
from Trains.serializers import TrainSerializer
from rest_framework import serializers

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

