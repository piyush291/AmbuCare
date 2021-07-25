from django.shortcuts import render, redirect ,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from hospital.models import *


from notifications.models import Notification
# Create your views here.

def ShowNotifications(request):
	id = request.user.id
	hospital_info = get_object_or_404(H_Details,user_id=id)
	notifications = Notification.objects.filter(hospital=hospital_info).order_by('-date')
	Notification.objects.filter(hospital=hospital_info, is_seen=False).update(is_seen=True)

	template = loader.get_template('misc/notifications.html')

	context = {
		'notifications': notifications,
	}

	return HttpResponse(template.render(context, request))

def DeleteNotification(request, noti_id):
	id = request.user.id
	hospital_info = get_object_or_404(H_Details,user_id=id)
	Notification.objects.filter(id=noti_id, hospital=hospital_info).delete()
	return redirect('notifications:ShowNotifications')


def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}

