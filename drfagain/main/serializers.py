from rest_framework import serializers
from .models import Animals

class AnimalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Animals     
        fields = '__all__' 