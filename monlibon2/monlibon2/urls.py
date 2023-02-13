
from django.contrib import admin
from django.urls import path

from shop2.views import index1, index2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index1),
    path('list/', index2)

]
