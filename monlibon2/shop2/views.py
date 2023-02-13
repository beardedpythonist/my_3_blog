from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index1(request):
    return HttpResponse('Привет лунатикам!!')


def index2(request):
    bbb = Parts.objects.all()
    return render(request, 'shop2/list.html', {'bbb': bbb})



    pass

# Create your views here.
