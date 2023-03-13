from rest_framework.serializers import ModelSerializer
from .models import *

class PartSerializer(ModelSerializer):

    class Meta:
        model = Parts
        fields = "__all__"



    def create(self, validated_data):
        return Parts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.brand = validated_data.get("brand", instance.brand)
        instance.artikul = validated_data.get("artikul", instance.artikul)
        instance.price = validated_data.get("price", instance.price)
        instance.rubric_id = validated_data.get("rubric_id", instance.rubric_id)
        instance.car_name_id = validated_data.get("car_name_id", instance.car_name_id)
        instance.save()
        return instance






