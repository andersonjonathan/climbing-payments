__author__ = 'jonathan'
from django import forms
from django.forms import ModelForm
from .models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'swish']


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'length', 'fee']


class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        exclude = ['trip']


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = ['where', 'when', 'driver','driver_shall_not_pay' ]


