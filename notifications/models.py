from django.db import models
from django.contrib.auth.models import User
from pat.models import P_Details
from hospital.models import H_Details

# Create your models here.

class Notification(models.Model):
	NOTIFICATION_TYPES = (
        (1,'Started'),
        (2,'Ended'), 
        (3,'Cancelled')
    )

	# ride = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name="noti_post", blank=True, null=True)
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_patient")
	hospital = models.ForeignKey(H_Details, on_delete=models.CASCADE, related_name="noti_to_hospital")
	notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)


