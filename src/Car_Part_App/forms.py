from django import forms
from .models import Car
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.db import  transaction

class Car_Part_Form(forms.ModelForm):
    class Meta:
        model=Car
        fields=[
            'Car_name',
            'Car_model',
            'Car_Part_Name',
            'Car_Part_Info',
            'category',
            'Car_Part_Discription',
            'Owner_info',
        ]

