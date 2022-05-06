from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests

# Create your views here.
def ping(request):
    return HttpResponse("pong")

@api_view()
def getPostOffice(request, PINCODE):
    url = f'https://api.postalpincode.in/pincode/{PINCODE}'
    response = requests.get(url)
    return Response(response.json())