from tkinter import Variable
from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from .models import contactUs
from datetime import datetime


# Create your views here.
def index(request):
    # context = {
    #     "Variable1":"this is Anmol Rastogi",
    #     "Variable2":"this is shabnam "
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is my home  page Anmol Rastogi")

def about(request):
    return render(request, 'about.html')
    

def services(request):
    return render(request, 'services.html')


def contactUs(request):

    if request.method =="POST":


        # name=request.POST.get("name")
        # number=request.POST.get("number")
        # email=request.POST.get("email")
        # age=request.POST.get("age")
    
        name = request.POST.get("name")
        number = request.POST.get("number")
        address = request.POST.get("address")
        state = request.POST.get("state")
        district = request.POST.get("district")
        village = request.POST.get("village")
        Password = request.POST.get("Password")
        c_pass = request.POST.get("c_pass")
        obj = contactUs(name=name,number=number,address=address,state=state,district=district,village=village,Password=Password,c_pass=c_pass)
        obj.save()
        
        return render(request, "contactUs.html")

        






    # obj = contactUs(name =name,number=number,email=email,age=age)
    # obj.save()
    
        
    
    



