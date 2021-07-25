from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'notifications'
urlpatterns = [
    path('ShowNotifications',views.ShowNotifications,name='ShowNotifications'),
    path('<noti_id>/delete', views.DeleteNotification, name='DeleteNotification'),
]