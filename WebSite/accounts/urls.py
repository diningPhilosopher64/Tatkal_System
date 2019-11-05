from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    path('',  views.user_base, name='user_base'),
    path('register/',  views.user_register, name='user_register'),
    path('login/',  views.user_login, name='user_login')
]