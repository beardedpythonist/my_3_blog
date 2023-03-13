
from django.contrib import admin
from django.urls import path
from shop2.views import *

urlpatterns = [path('admin/', admin.site.urls),
               path('api/v1/partslist/', PartsAPInew.as_view(), name='apiparts'),
               path('api/v1/partslist/<int:pk>/', PartsAPInew.as_view()),
               path('', index)
  ]


