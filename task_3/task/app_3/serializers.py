from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    district = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

