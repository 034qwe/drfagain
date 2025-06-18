from django.shortcuts import render
from rest_framework import generics
from .models import Animals, Category_Animals
from .serializers import AnimalSerializer

class AnimalsAPIView(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


class AnimalAPIUpdate(generics.UpdateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer