from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Driver, Car



class DriverForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = ["username", "password1", "password2", "email", "license_number"]
        widgets = {
            'password':  forms.PasswordInput(),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "model"]


class CarSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
    )
