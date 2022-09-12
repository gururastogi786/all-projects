from rest_framework import serializers
from .models import *


# class StateSerializer(serializers.Serializer):
#     s_name=serializers.CharField(max_length=100)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        models= State
        fields="__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        models= District
        fields="__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         models= User
#         fields=['u_name','email','password']


# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         models= Subscription
#         fields="__all__"

# class FreeSerializer(serializers.ModelSerializer):
#     class Meta:
#         models= Free
#         fields="__all__"