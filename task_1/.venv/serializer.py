from rest_framework import serializers
from app_1.models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        field="__all__"