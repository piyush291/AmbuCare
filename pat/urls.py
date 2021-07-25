from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('activity',views.activity,name='activity'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('register',views.register,name='register'),
    path('register_patient',views.register_patient,name='register_patient'),
    # path('register_photo',views.register_photo,name='register_photo'),   
    path('directions',views.directions,name='directions'),   
 ]
