from .models import *
from Trains.serializers import TrainSerializer
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    train_id = TrainSerializer()

    class Meta:
        model = Booking
        fields = (
            'id',         
            'train_id',
            'date',
            'user_id',
        )

