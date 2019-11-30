from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'dashboard' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    
    path('',  views.train_list, name='train-list'),
    path('bookings/',  views.booking_list, name='booking-list'), 
]