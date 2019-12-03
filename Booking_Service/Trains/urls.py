from django.urls import path
from .views import *

urlpatterns = [

    # Train API
    path('', TrainList.as_view(), name = 'train-list' ),
    path('<int:pk>', TrainDetail.as_view(), name = 'train-detail' ),
    path('<int:train_id>/<int:tickets_left>', ConsumeTicket.as_view(), name = 'consume-ticket' ),
    

]
