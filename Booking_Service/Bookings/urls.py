from django.urls import path
from .views import *

urlpatterns = [

    # Bookings API
    
    path('<int:user_id>', BookingList.as_view(), name = 'bookings-list' ),
    # path('detail/<int:booking_id>', BookingDetail.as_view(), name = 'booking-detail' ),
    path('all', AllBookings.as_view(), name='all-bookings-list' )
]
