from django.db import models
from django.urls import reverse
from pat.models import P_Details
from hospital.models import *
# Create your models here.

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"


class hospital(models.Model):
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    lat  = models.DecimalField(max_digits=11, decimal_places=7)
    lon  = models.DecimalField(max_digits=11, decimal_places=7)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        # return "blog/%d" %(self.id)
        return reverse("show_hospital", args=[(self.id)])
        