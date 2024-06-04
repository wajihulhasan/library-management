
from django import forms

from locations.models import Location, LOCATION_TYPE_CHOICES


class LocationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    capacity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(widget=forms.Select(choices=LOCATION_TYPE_CHOICES,attrs={'class': 'form-control'}))

    class Meta:
        model = Location
        fields = '__all__'