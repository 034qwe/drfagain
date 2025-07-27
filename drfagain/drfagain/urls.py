
from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers


router = routers.SimpleRouter()
# router.register('animal',AnimalViewSet, basename='animal')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('animals/', AnimalsAPIView.as_view()),
    path('animals/<int:pk>/', AnimalAPIUpdate.as_view()),
    path('animalsdelete/<int:pk>/', AnimalAPIDestroy.as_view()),
    # path('', include(router.urls))

 ]
