from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'polls'

urlpatterns = [
    path('details/<int:id>/',views.details,name='details'),
    path('results/<int:id>/',views.results,name='results'),
    path('vote/<int:id>/', views.vote, name='vote')
]
