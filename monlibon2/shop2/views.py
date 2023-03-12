from django.forms import *
from django.views.generic import *
from rest_framework.views import APIView
from rest_framework.response import *
from .models import *
from .serializer import *


class PartsApiView(APIView):
    def get(self, request):
        ls = Parts.objects.all().values()
        return Response({'posts': PartSerializer(ls, many=True).data})
    def post(self, request):
        newpart = Rubric.objects.create(
            name  = request.data['name'],
        )
        return Response({'parts':model_to_dict(newpart)} )

