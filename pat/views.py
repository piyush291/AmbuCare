from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from hospital.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth

# Create your views here.

def index(request):
    print("login")
    bookings_info = Bookings.objects.filter(user_id=request.user.id)
    h_info = H_Details.objects.all()

    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('index')
            else:
                return HttpResponse("user is not active")
        else:
            print('views ke andar user_login mein')
            return HttpResponse("user is none")
            
    else:
        return render(request,'misc/index.html',{'bookings_info':bookings_info,'h_info':h_info})

    
def logout(request):
    auth.logout(request)
    return redirect ('index')



def activity(request):
    return render(request,'misc/activity.html')

def aboutus(request):
    return render(request,'misc/aboutus.html')


        
        

def register(request):
    form=None
    if request.method =="POST":
        print("views mein")
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            print('chal raha hai')
            new_user=form.save()
            new_user.set_password(form.cleaned_data['password'])
            # new_user=User.objects.create_user()
            new_user.save()
            return redirect('index')
    else:
        print("else waala part")
        form=UserRegistrationForm()
    context={
        'form' : form
    }
    print("idhar bhi")
    return render(request,'misc/register.html',context)





def register_patient(request):
    
    print('hello')
    if request.method =='POST':
        print('Post ke andar')

        profile_form = P_DetailsForm(data=request.POST or None,files=request.FILES)
        if profile_form.is_valid():
            print('validated')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            # img=request.POST.get('img')
            city=request.POST.get('city')
            state=request.POST.get('state')
            zip=request.POST.get('zip')
            timestamp=request.POST.get('timestamp')
            
            details1 = P_Details.objects.create(address=address,phone=phone,city=city,state=state,zip=zip,timestamp=timestamp,user=request.user)
            details1.save()
            return redirect('index')
             
    else:
        profile_form = P_DetailsForm()
    
    context={
        'profile_form': profile_form
    }  
    return render(request,'pat/register_patient.html',context)





def directions(request):
    return render(request,'directions.html')





