from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/',  views.register_user, name='user-register'),
    path('login/',  views.login_user, name='login'),
    # path('logout/', views.user_logout, name='user_logout')
]