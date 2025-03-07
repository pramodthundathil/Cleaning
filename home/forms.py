from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
from django import forms


class UserAddForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        # fields = "__all__"
        fields = ["username","phone","pro_pic","email","first_name","last_name","password1","password2"]


        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            "pro_pic":forms.FileInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "first_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
        
        }

    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password confirmation'})


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        # fields = "__all__"
        fields = ["username","phone","pro_pic","email","first_name","last_name","password"]


        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            "pro_pic":forms.ClearableFileInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "first_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
        
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password'})
       

from django import forms
from .models import Service, Service_booking

from .models import Service, Service_booking

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_category', 'rate_per_hour', 'description']
        widgets = {
            'service_category': forms.Select(attrs={'class': 'form-control'}),
            'rate_per_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = Service_booking
        fields = ['booked_date', 'description']
        widgets = {
            'booked_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
