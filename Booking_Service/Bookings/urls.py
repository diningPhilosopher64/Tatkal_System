from django.urls import path
from .views import *

urlpatterns = [

    # Bookings API
    
    path('', BookingList.as_view(), name = 'bookings-list' ),
    path('<int:pk>', BookingDetail.as_view(), name = 'booking-detail' ),
    path('all', AllBookings.as_view(), name='all-bookings-list' )
]
