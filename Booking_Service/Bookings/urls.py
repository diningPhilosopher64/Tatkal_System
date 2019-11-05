from django.urls import path
from .views import *

urlpatterns = [
   
    # Bookings API
    path('', BookingList.as_view(), name = 'booking-list' ),
    path('<int:pk>', BookingDetail.as_view(), name = 'booking-detail' ),

]
