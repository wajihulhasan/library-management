
from django import forms

from positions.models import Position


class PositionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    responsibility = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Position
        fields = '__all__'
