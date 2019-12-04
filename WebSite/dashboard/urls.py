from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('',  views.dashboard, name='dashboard'),
    path('bookings/',  views.user_bookings, name='user-bookings'),
    path('book/<int:train_id>/<int:tickets_left>', views.book_ticket, name = 'book-ticket'),


    
    # path('logout/', views.user_logout, name='user_logout')
]