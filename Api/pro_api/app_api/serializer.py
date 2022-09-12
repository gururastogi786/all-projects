from pyexpat import model
from rest_framework import serializers
from app_api.models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = "__all__"