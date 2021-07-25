from django.db import models
from django.contrib.auth.models import User
from pat.models import *
from hospital.models import H_Details
from .models import *

from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

@receiver(post_save,sender = Bookings)
def create_notifications(sender,instance,created,**kwargs):
    print('sender ',sender)
    print('instance ',instance)
    print('created ',created) 
    print('kwargs ',kwargs)
    if created:
        print('inside if')
        obj = Notification.objects.create(patient = instance.user,hospital=instance.hospital,notification_type=1)
        obj.save()

