from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse

def createEvent(request):
    