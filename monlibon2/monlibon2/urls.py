
from django.contrib import admin
from django.urls import path
from shop2.views import index, shop

urlpatterns = [path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('shop/',shop, name= 'shop')]


