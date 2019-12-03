from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('',  views.dashboard, name='dashboard'),
    
    # path('logout/', views.user_logout, name='user_logout')
]