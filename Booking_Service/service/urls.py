from django.urls import path
from .views import *
urlpatterns = [
    # Train API
    path('', TrainList.as_view(), name = 'train-list' ),
    path('<int:pk>', TrainDetail.as_view(), name = 'train-detail' ),

    path('bookings', BookingList.as_view(), name = 'booking-list' ),
    path('bookings/<int:pk>', BookingDetail.as_view(), name = 'booking-detail' ),


]
