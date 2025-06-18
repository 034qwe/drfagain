from rest_framework import serializers
from .models import Animals

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals     
        fields = ('title', 'price','description', 'categ')