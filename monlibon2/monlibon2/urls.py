
from django.contrib import admin
from django.urls import path
from shop2.views import *

urlpatterns = [path('admin/', admin.site.urls),
    path('api/v1/partslist/', PartsApiView.as_view(), name='apiparts')
  ]


