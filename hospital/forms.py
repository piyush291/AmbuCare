from .models import H_Details,Ambulance,Driver,Doctor
from django import forms
from django.forms import ModelForm


class H_DetailsForm(ModelForm):
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here','rows':'1','cols':'10'}))
    phone=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here','rows':'1','cols':'10'}))
    city=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here','rows':'1'}))
    state=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here','rows':'1','cols':'10'}))
    class Meta:
        model=H_Details
        fields = ['certi_img','address','phone', 'city', 'state']


    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password mismatch")
        return confirm_password



class AmbulanceForm(ModelForm):
    class Meta:
        model=Ambulance
        fields = ['img','num_plate']


class DriverForm(ModelForm):
    class Meta:
        model=Driver
        fields = ['img','phone','driving_license']


class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields = ['specialization','name','duty_start','duty_end','img']