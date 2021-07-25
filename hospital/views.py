from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from hospital.forms import H_DetailsForm,AmbulanceForm,DriverForm,DoctorForm
from .models import *
from django.contrib.auth.models import auth,User
from django.forms import modelformset_factory

# Create your views here.

def HOSPITAL(request):
    hospital_list = H_Details.objects.all()
    context={
        'hospital_list':hospital_list,
    }

    return render(request,'hospitals/HOSPITAL.html',context)

def changes(request):
    return render(request,'misc/changes.html')

def register_hospital(request):
    form=None
    if request.method =='POST':
        form = H_DetailsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("galat")

    else:
        form = H_DetailsForm()
    context={
        'form':form,
    }
    return render(request,'hospitals/register_hospital.html',context)


def register_ambulance(request):
    form=None
    if request.method =='POST':
        form = AmbulanceForm(request.POST or None,request.FILES or None)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("galat")

    else:
        form = AmbulanceForm()
    context={
        'form':form,
    }
    return render(request,'hospitals/register_ambulance.html',context)


def register_driver(request):
    form=None
    if request.method=="POST":
        form = DriverForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            print("image")
            return redirect('index')
        else:
            print("sorry")
    else:
        form=DriverForm()
    context = {
        'form':form,
    }
    return render(request,'hospitals/register_driver.html',context)


def register_doctor(request):
    if request.method=="POST":
        form = DoctorForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            print("image")
            return redirect('index')
        else:
            print("sorry")
    else:
        form=DoctorForm()
        context = {
            'form':form,
        }
        return render(request,'hospitals/register_doctor.html',context)
    

# def show_hospital(request,id):
#     print(id)
#     patient_id = request.user.id
#     print(patient_id)
#     patient_info = get_object_or_404(P_Details,user_id=patient_id)
#     hospital_info = get_object_or_404(H_Details,id=id)
#     context = {
#         'hospital_info': hospital_info,
#         'patient_info':patient_info,
#         }   
#     print('hello')
#     return render(request,'maps/final_map.html',context)


def list1(request):
    hospital_list = H_Details.objects.all()
    context = {
        'hospital_list':hospital_list
    }
    return render(request,'hospitals/hospital_list.html',context)

   

