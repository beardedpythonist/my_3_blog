
from django.contrib import admin
from django.urls import path
from shop2.views import *

urlpatterns = [path('', index),
               path('admin/', admin.site.urls),
               path('api/v1/partslist/', PartsAPInew.as_view(), name='apiparts'),
               path('api/v1/partslist/<int:pk>/', PartsAPIUpdate.as_view()),
                   path('api/v1/partsdetail/<int:pk>/', PartsAPIDetail.as_view())
  ]


