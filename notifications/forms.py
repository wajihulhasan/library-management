
from django import forms

from notifications.models import Notification
from patrons.models import Patron


class NotificationForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Notification
        fields = '__all__'
