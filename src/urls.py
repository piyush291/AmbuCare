from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'src'

urlpatterns = [
    path('',views.calculateDistView,name='calculateDist'),  
    path('javascript',views.javascript,name='javascript'),
    path('flask',views.index,name='flask'),
    path('<int:id>/',views.show_hospital,name="show_hospital"),
    path('present_location',views.present_location,name='present_location'),
    path('final',views.final,name='final'),
    path('<int:id>/booked/',views.booked,name='booked'),
 ]
