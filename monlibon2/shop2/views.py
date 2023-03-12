from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from .models import *




class PartsView(ListView):
    model = Parts
    template_name = 'shop2/index.html'
    context_object_name = 'parts'

