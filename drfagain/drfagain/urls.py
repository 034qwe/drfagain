
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView,  TokenVerifyView


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
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  JWT TOken auth

    # path('', include(router.urls))

 ]
