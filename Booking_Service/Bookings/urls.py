from django.urls import path
from .views import *

urlpatterns = [

    # Bookings API    
    path('<int:user_id>', BookingList.as_view(), name = 'bookings-list' ),
    path('all', AllBookings.as_view(), name='all-bookings-list' ),
    path('<int:user_id>/<int:train_id>', AddBooking.as_view() ,name='add-booking' )

    
]
