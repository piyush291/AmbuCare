from django.db import models
from django.contrib.auth.models import User
from notifications.models import *
from hospital.models import H_Details
from .models import *

from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver

@receiver(post_delete,sender = Notification)
def update_bookings(sender,instance,**kwargs):
    print("hello")
    print()
    print('sender ',sender)
    print('instance ',instance) 
    print('kwargs ',kwargs)
    print()
    obj = Bookings.objects.get(user = instance.patient)
    obj.status = "Cancelled By Driver"
    print("done")
    obj.save()