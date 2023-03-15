from django.forms import *
from django.shortcuts import *
from django.views.generic import *
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, mixins, GenericViewSet

from shop2.perm import IsOwnerOrReadOnly
from .models import *
from .serializer import *


class PartViewSetCreate(ListCreateAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartSerializer
    permission_classes = (IsAuthenticated,)


class PartViewSetCreateUpdate(RetrieveUpdateAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartSerializer
    permission_classes = (IsAuthenticated,)

    # взял код из документации и  создал свой  перм https://www.django-rest-framework.org/api-guide/permissions
    # permission_classes = (IsOwnerOrReadOnly,)


class PartViewSetDelete(DestroyAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartSerializer
    permission_classes = (IsAdminUser,)

#
# def get_queryset(self):
#             return Parts.objects.all()[0:4]
#         @action(methods=["GET"], detail=True)
#         def rubric(self, request, pk=None):
#             rubs =  Rubric.objects.get(pk=pk)
#             return Response({'rubs': rubs.name})
# class PartsAPInew(generics.ListCreateAPIView):
#     queryset = Parts.objects.all()
#     serializer_class = PartSerializer
#
#
# class PartsAPIUpdate(generics.UpdateAPIView):
#     queryset = Parts.objects.all()
#     serializer_class = PartSerializer
#
# class PartsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Parts.objects.all()
#     serializer_class = PartSerializer

#
# class PartsApiView(APIView):
#     def get(self, request):
#         ls = Parts.objects.all().values()
#         return Response({'posts': PartSerializer(ls, many=True).data})
#
#     def post(self, request):
#         serializer = PartSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'parts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Parts.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = PartSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})

def index(request):
    part = Parts.objects.all()
    context = {'part': part}
    return render(request, 'shop2/index.html', context)
