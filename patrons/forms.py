
from django import forms

from patrons.models import Patron, STATUS_CHOICES


class PatronForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    membership_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))
    membership_status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Patron
        fields = '__all__'
