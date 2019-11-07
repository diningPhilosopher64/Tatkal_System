from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'dashboard' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    
    path('',  views.trainList, name='train-list'), 
]