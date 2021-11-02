from django.shortcuts import render
from django.http import HttpResponse
from api import models
import requests

# Create your views here
def index(request,link_id,user_id):
    a = models.Api.objects.get(personal_id = str(link_id))
    q = a.quantity
    a.quantity = q+1
    a.save()
    return HttpResponse("hello world")