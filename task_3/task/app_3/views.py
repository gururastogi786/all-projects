import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def User(request):
    if request.method == "POST":
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parser(data=pythondata)
        serializer = UserSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')