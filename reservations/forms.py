
from django import forms

from reservations.models import Reservation


class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reservation
        fields = '__all__'
