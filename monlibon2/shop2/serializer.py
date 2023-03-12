from rest_framework import serializers
from .models import *


class PartSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=50)
    artikul = serializers.CharField()
    price = serializers.FloatField()
    # rubric = serializers.CharField()
    # Car_name = serializers.CharField()
