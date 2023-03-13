from django.contrib import admin
from django.urls import path, include
from shop2.views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'parts',  PartViewSet)


urlpatterns = [path('', index),
               path('admin/', admin.site.urls),
               path('api/v1/', include(router.urls))]
