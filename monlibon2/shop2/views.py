from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'shop2/index.html')

def shop(request):
    return render(request, 'shop2/shop.html')
