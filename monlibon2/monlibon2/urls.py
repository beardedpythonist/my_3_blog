import rest_framework
from django.contrib import admin
from django.urls import path, include, re_path
from shop2.views import *

from rest_framework import routers



urlpatterns = [path('', index),
               path('admin/', admin.site.urls),
               path('api/v1/auth-session/', include('rest_framework.urls')),  # подключаем к  аутентификации
               path('api/v1/parts/', PartViewSetCreate.as_view() ),
               path('api/v1/parts/<int:pk>', PartViewSetCreateUpdate.as_view()),
               path('api/v1/partsdelete/<int:pk>', PartViewSetDelete.as_view()),
               path('api/v1/auth/', include('djoser.urls')),
               re_path(r'^auth/', include('djoser.urls.authtoken')),
               ]