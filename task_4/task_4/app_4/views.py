# from django.shortcuts import render
# from .serializers import StateSerializer,DistrictSerializer,UserSerializer
# from .models import State,District,User
# from rest_framework import viewsets

# from os import stat
# from django.shortcuts import render
# from rest_framework.views import APIView
# from app_4.models import *
# from app_4.serializers import *
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework import status
# # Create your views here.

# -------------------------------------------------------------------------------

























































# class ListState(APIView):
#     def get(self, request):
#         try:
#             sta = State.objects.all()
#             serializer = StateSerializer(sta, many=True)
#             return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


# class Districtapi(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             sta = State.objects.get(id=data['id'])
#             dis = District.objects.filter(state=sta)
#             serializer = DistrictSerializer(dis, many=True)
#             return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


# class Showuserapi(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             usr = UserPro.objects.get(id=data['id'])
#             serializer = UserSerializer(usr)
#             data = dict(serializer.data) | {"state_name": usr.state.name, "district_name": usr.district.name}
#             return Response({"status_code": status.HTTP_200_OK,"data":data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)




# class Userapi(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             sta = State.objects.get(id=data['state'])
#             dis = District.objects.get(id=data['district'])
#             serializer = UserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save(
#                     state=sta,
#                     district=dis
#                 )
#             return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


# --------------------------------------------------------
# class StateViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class DistrictViewSet(viewsets.ModelViewSet):
#     queryser = District.objects.all()
#     serializer_class = DistrictSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# ----------------------------------------------------------

