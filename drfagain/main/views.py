from django.shortcuts import render
from rest_framework import generics
from .models import Animals, Category_Animals
from .serializers import AnimalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .mypermissions import *

class AnimalsAPIView(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AnimalAPIUpdate(generics.UpdateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsOwnerOrReadOnly)

class AnimalAPIDestroy(generics.DestroyAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


# class AnimalViewSet(viewsets.ModelViewSet):
#     # queryset = Animals.objects.all()
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if pk:
#             return Animals.objects.filter(pk=pk)
#         else:
#             return Animals.objects.all()


#     serializer_class = AnimalSerializer
