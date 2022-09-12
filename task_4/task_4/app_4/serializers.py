from dataclasses import fields
from rest_framework import serializers
from .models import *

# ------------------------------------------------------
# class StateSerializer(serializers.Serializer):
#     class Meta:
#         model = State
#         fields = ['id',"state_name"]

# class DistrictSerializer(serializers.Serializer):
#     class Meta:
#         model = District
#         fields =['id',"s_name","dict_name"]

# class UserSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         field ="__all__"
    
# -------------------------------------------------------

from rest_framework import serializers
from app_4.models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPro
        fields = "__all__"
