from .models import P_Details
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User,auth


class UserRegistrationForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder': 'Enter the password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder': 'confirm password'}))

    print('class waali jagah')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password mismatch")
        return confirm_password


class P_DetailsForm(ModelForm):
    
    class Meta:
        model = P_Details
        exclude = ("user",)



# class ImagesForm(ModelForm):
#     class Meta:
#         model = Images
#         fields = ("image")