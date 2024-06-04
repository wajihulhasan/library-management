
from django import forms

from fines.models import Fine, FINE_STATUS_CHOICES


class FineForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reason = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=FINE_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Fine
        fields = '__all__'
