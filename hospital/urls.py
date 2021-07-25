from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'hospital'
urlpatterns = [
    path('HOSPITAL',views.HOSPITAL,name='HOSPITAL'),
    path('changes',views.changes,name='changes'),
    path('register_hospital',views.register_hospital,name='register_hospital'),
    path('register_driver',views.register_driver,name='register_driver'),
    path('register_ambulance',views.register_ambulance,name='register_ambulance'),
    path('register_doctor',views.register_doctor,name='register_doctor'),
    # path('<int:id>/',views.show_hospital,name="show_hospital"),
    path('hospital_list',views.list1,name="list1")
 ]
 
