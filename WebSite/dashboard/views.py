from django.shortcuts import render
from accounts.models import Account
from django.views.generic import (
    DetailView,
    ListView,
)
import requests
import json

# Create your views here.



def trainList(request):
    URL = "http://bookingService:8000/trains/" 
    content = requests.get(url = URL)
    print("Contents are \n\n\n\n\n")
    print(content.text)
    content = json.loads(content)
    context = {
        "trains" : content
    }

    return render(request, 'dashboard/dashboard.html', context=context)

# class TrainListView(ListView):
#         template = "dashboard/dashboard.html"

#      def get_queryset(self):
#         URL = "bookingService:8000/trains/"
#         user = Account
#         PARAMS = {'user':Account}         
#         content = requests.get(url = URL, params = PARAMS)
#         print("Contents are \n\n\n\n\n")
#         print(content.text)
#         return json.loads(content)
            
 



