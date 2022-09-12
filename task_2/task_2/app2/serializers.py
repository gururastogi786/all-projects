from sre_parse import State
from rest_framework import serializers
from app2.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","user_name","add","email"]


# class StateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = State
#         fields = ["id","state_name"]


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["s_name","name","state","email"]
