from rest_framework.serializers import ModelSerializer
from .models import *

class PartSerializer(ModelSerializer):

    class Meta:
        model = Parts
        fields = "__all__"