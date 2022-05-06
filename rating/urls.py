from django.urls import path 
from . import views
from .data import create_movie_entries

#function to create initial data, run one time only
#create_movie_entries()

urlpatterns = [
    path('ping', views.ping, name="ping"),
    path('postoffice/<PINCODE>', views.getPostOffice, name="getPostOffice"),
]
