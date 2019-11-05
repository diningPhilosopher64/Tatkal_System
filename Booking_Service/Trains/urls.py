from django.urls import path
from .views import *

urlpatterns = [

    # Train API
    path('', TrainList.as_view(), name = 'train-list' ),
    path('<int:pk>', TrainDetail.as_view(), name = 'train-detail' ),

]
