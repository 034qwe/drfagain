
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import *
from rest_framework import routers


router = routers.SimpleRouter()
# router.register('animal',AnimalViewSet, basename='animal')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('settings/auth/', include('rest_framework.urls')),
    path('animals/', AnimalsAPIView.as_view()),
    path('animals/<int:pk>/', AnimalAPIUpdate.as_view()),
    path('animalsdelete/<int:pk>/', AnimalAPIDestroy.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('', include(router.urls))

 ]
