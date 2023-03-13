from django.contrib import admin
from .models import *
class PartsAdmin(admin.ModelAdmin) :
    list_display = ('name', 'artikul', 'price', 'rubric', 'car_name')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Parts, PartsAdmin)
admin.site.register(Rubric)
admin.site.register(Car_name)


