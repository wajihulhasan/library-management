
from django import forms

from eventRegistration.models import EventRegistration


class EventRegistrationForm(forms.ModelForm):
    registration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = EventRegistration
        fields = '__all__'
