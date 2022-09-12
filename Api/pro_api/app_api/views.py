from django.shortcuts import render
from app_api.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_api.serializer import *

# Create your views here.
def index(request):
    department=Department.objects.all() 
    employee=Employee.objects.all()
    product=Product.objects.all() 
    context={
        "department":department,
        "product":product,
        "employee":employee,
    }
    
    print("department: ", department)
    print("employee: ", employee)
    print("product: ", product)
    return render(request,'index.html',context)



# @api_view(['POST'])
# def Er_Anmol_Rastogi(request):
#     data = request.data
#     try:
#         emp = Employee.objects.get(id=data["id"])
#         serializer = EmployeeSerializer(emp)
#         return Response({"status_code": status.HTTP_200_OK,"message": "Data getting successfully.", "data": serializer.data}, status= status.HTTP_200_OK)
#     except:
#         return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)
        


@api_view(['POST'])
def Er_Anmol_Rastogi(request):
    data = request.data
    try:
        emp = Employee.objects.get(id=data["id"],Adhar_number=data["Adhar_number"],name=data["name"])
        serializer = EmployeeSerializer(emp)
        return Response({"status_code": status.HTTP_200_OK,"message": "Data getting successfully.", "data": serializer.data}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)    
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)
        







@api_view(['POST'])
def add_dept(request):
    data = request.data
    try:
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # Department(dept_name=data["dept_name"],email=data["email"]).save()
        
        return Response({"status_code": status.HTTP_200_OK,"message": "Data save successfully."}, status= status.HTTP_200_OK)
    except:
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_emp(request):
    data = request.data
    try:
        adhar = Adhar.objects.get(Adhar_number=12)
        dept = Department.objects.get(dept_name=data["department"])
        # serializer = EmployeeSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save(
        #         adhar = adhar,
        #         dept = dept
        #     )
        Employee(adhar=adhar, emp_name=data["name"], dept=dept, email=data["email"]).save()
        # Department(dept_name=data["dept_name"],email=data["email"]).save()
        
        return Response({"status_code": status.HTTP_200_OK,"message": "Data save successfully."}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_emp(request):
    data = request.data
    try:
        emp = Employee.objects.get(id=data["id"])
        emp.emp_name = data["name"]
        emp.email = data["email"]
        emp.save()
        
        return Response({"status_code": status.HTTP_200_OK,"message": "Data save successfully."}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def delete_adhar(request):
    data = request.data
    try:
        Adhar.objects.get(Adhar_number=data["Adhar_number"]).delete()
        return Response({"status_code": status.HTTP_200_OK,"message": "Data save successfully."}, status= status.HTTP_200_OK)
    except:
        return Response({"status_code": status.HTTP_404_NOT_FOUND,"message": "Data not found."}, status= status.HTTP_404_NOT_FOUND) 


# def emp(request):
#     employee=Employee.objects.all()
#     print("employee: ", employee)
#     return render(request,'emp.html',{"employee":employee})

# def product(request):
#     product=Product.objects.all
#     print("prod: ", product)
#     return render(request,'product.html',{"product":product})

