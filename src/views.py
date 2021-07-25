from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo , get_center_coordinates , get_zoom
import folium
from django.views.generic import ListView
import datetime

from django.db import models
from django.contrib.auth.models import User
from pat.models import *
from hospital.models import *


import requests
import smtplib


# Create your views here.


# pip install folium
# pip install geoip

# video from pyplane

# pip install geomaps : not used , but can be seen from gfg

def calculateDistView(request):
    distance = None
    destination = None
    #obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent="src")

    ip = '103.21.127.114'
    country,city,lat,lon = get_geo(ip)

    l_lat=lat
    l_lon=lon
    pointA = (l_lat,l_lon)
    m = folium.Map(width=1100,height=630,location=get_center_coordinates(l_lat,l_lon),zoom_start=8)

    folium.Marker([l_lat,l_lon],tooltip= 'click here for more info',popup=city['city'],icon=folium.Icon(color='red')).add_to(m)

    if form.is_valid():
        instance=form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        
        print(destination)
        print(destination_)
        print('location',country)
        location = geolocator.geocode(city)
        print('###############',location)
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat,d_lon)

        distance = round(geodesic(pointA,pointB).km,2)

        m = folium.Map(width=1100,height=630,location=get_center_coordinates(l_lat,l_lon,d_lat,d_lon),zoom_start=get_zoom(distance))

        folium.Marker([l_lat,l_lon],tooltip= 'click here for more info',popup=city['city'],icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([d_lat,d_lon],tooltip= 'click here for more info',popup=destination,icon=folium.Icon(color='purple',icon="cloud")).add_to(m)

        line = folium.PolyLine(locations=[pointA,pointB],weight=2,color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance':distance,
        'destination':destination,
        'form': form,
        'map':m,
    }

    return render(request,'distance.html',context)


def javascript(request):
    return render(request,'misc/googleMaps.html')


def index(request):
    hospital_list = hospital.objects.all()
    context = {
        'hospital_list': hospital_list,
    }
    return render(request,'maps/index1.html', context)



def show_hospital(request,id):
    print(id)  # id of hospital from H_Details
    patient_id = request.user.id
    print(patient_id) # id of patient from user
    

    patient_info = get_object_or_404(P_Details,user_id=patient_id)
    hospital_info = get_object_or_404(H_Details,id=id)

    hospital_id = hospital_info.user_id    # id of hospital from user  or user_id from H_Details ; for NHS it should be 3
    print(hospital_info.user_id)

    driver_info = get_object_or_404(Driver,user_id=hospital_id)
    ambulance_info = get_object_or_404(Ambulance,user_id=hospital_id)
    # doctor_info = get_object_or_404(Doctor,user_id=hospital_id)
    doctors_info = Doctor.objects.filter(user_id=hospital_id)


    # presnt_time = datetime.datetime.now()    #class datetime.datetime
    present_time = datetime.datetime.now().time() # datetime.time
    print(type(present_time))
    print(present_time)
    # doctor_info  = doctors_info[0]
    for doctor in doctors_info:
        print(type(doctor.duty_start))          # datetime.time
        print('start',doctor.duty_start)
        print('end',doctor.duty_end)
        if doctor.duty_start < present_time or doctor.duty_end > present_time:
            print('inside if')
            doctor_info = doctor
            break


    context = {
        'hospital_info': hospital_info,
        'patient_info':patient_info,
        'doctor_info':doctor_info,
        'ambulance_info':ambulance_info,
        'driver_info':driver_info,
        }   
    print('hello')
    print(ambulance_info.num_plate)
    return render(request,'maps/final_map.html',context)


def booked(request,id):
    # id is id of hospital from H_DETAILS
    patient_info = get_object_or_404(P_Details,user_id=request.user.id)
    hospital_info = get_object_or_404(H_Details,id=id)
    user_info = get_object_or_404(User,id=request.user.id)
    obj = Bookings.objects.create(hospital_id=id ,user_id = request.user.id)
    print('hi')
    obj.save()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('piyushsethi291@gmail.com','heypiy8782')

    subject='Ride booked'
    h_add = hospital_info.address
    p_add = patient_info.address
    p_email = user_info.email
    body='Your booking is successful. Ambulance from ' + h_add + ' is coming to '+ p_add

    msg = f"Subject :{subject}\n\n{body}"

    server.sendmail(
        'piyushsethi291@gmail.com',   # sender
        p_email,    # receiver
        msg
    )

    print("email has been sent")
    hospital_id = hospital_info.user_id
    driver_info = get_object_or_404(Driver,user_id=hospital_id)
    ambulance_info = get_object_or_404(Ambulance,user_id=hospital_id)

    context = {
        'hospital_info': hospital_info,
        'patient_info':patient_info,
        'ambulance_info':ambulance_info,
        'driver_info':driver_info,
        }  


    return render(request,'misc/done.html',context)












def present_location(request):
    return render(request,'maps/present_location.html')


def final(request):
    print('kya hua')
    #id = request.user.id   #by this we are getting id from user table but we want from P_Details
    # but we somehow have to pass id of P_details
    print(id)
    patient_info = get_object_or_404(P_Details,id=id)

    print(patient_info.address)
    context = {
        'patient_info': patient_info,
    }

    return render(request,'maps/final_map.html',context)
