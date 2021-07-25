from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User
from hospital.models import *


# Create your models here.


class P_Details(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    # img = models.ImageField( upload_to="pics/", blank=True,null=True)
    city = models.TextField()
    state = models.TextField()
    zip = models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(H_Details, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,blank=True,null=True,editable=True)


