from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User
from pat.models import *
from django.urls import reverse

# Create your models here.

class H_Details(models.Model): 
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    certi_img = models.ImageField(upload_to='hospital',blank=True,null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # return "blog/%d" %(self.id)
        return reverse("show_hospital", args=[(self.id)])

class Ambulance(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='ambulance',blank=True,null=True)
    num_plate=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Driver(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    driving_license = models.ImageField(upload_to='driver',blank=True,null=True)
    img = models.ImageField(upload_to='driver',blank=True,null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)




class Doctor(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    img = models.ImageField(upload_to='Doctor',blank=True,null=True)
    duty_start=models.TimeField(auto_now=False, auto_now_add=False,default="12:00:00")
    duty_end=models.TimeField(auto_now=False, auto_now_add=False,default="12:00:00")