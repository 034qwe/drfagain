from django.shortcuts import render
from rest_framework import generics
from .models import Animals, Category_Animals
from .serializers import AnimalSerializer
from rest_framework import viewsets

# class AnimalsAPIView(generics.ListCreateAPIView):
#     queryset = Animals.objects.all()
#     serializer_class = AnimalSerializer


# class AnimalAPIUpdate(generics.UpdateAPIView):
#     queryset = Animals.objects.all()
#     serializer_class = AnimalSerializer

# class AnimalAPIMore(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Animals.objects.all()
#     serializer_class = AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    # queryset = Animals.objects.all()
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Animals.objects.filter(pk=pk)
        else:
            return Animals.objects.all()
        
            
            
            
    serializer_class = AnimalSerializer
