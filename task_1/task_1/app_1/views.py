from django.shortcuts import render
from app_1.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_1.serializer import *
# Create your views here.


@api_view(['GET'])
def insert_data(request):
    try:
        emp = State.objects.values()    
        serializer = StateSerializer(emp, many=True)
        
        # json_data = JSONRenderer().render(serializer.data)
        return Response({"status_code": status.HTTP_200_OK,"message": "Data getting successfully.", "data": serializer.data}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)    
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)
        


    
@api_view(['POST'])
def district(request):
    data = request.data
    try:
        state = State.objects.get(id=data['id'])
        emp = District.objects.filter(state_dist=state)
        serializer = DistrictSerializer(emp, many = True)
        # json_data = JSONRenderer().render(serializer.data)
        return Response({"status_code": status.HTTP_200_OK,"message": "Data getting successfully.", "data": serializer.data}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)    
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def User(request):
    data = request.data
    try:
        state = State.objects.get(id=data['id'])
        emp = District.objects.filter(state_dist=state)
        serializer = DistrictSerializer(emp, many = True)
        # json_data = JSONRenderer().render(serializer.data)
        return Response({"status_code": status.HTTP_200_OK,"message": "Data getting successfully.", "data": serializer.data}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)    
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)
    

