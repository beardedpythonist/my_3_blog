from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class PartSerializer(ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Parts
        fields = "__all__"