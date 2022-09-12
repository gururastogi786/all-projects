from django.shortcuts import render
from rest_framework import generics
from app2.models import User 
from app2.serializers import UserSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer


