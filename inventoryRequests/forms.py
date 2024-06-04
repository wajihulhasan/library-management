
from django import forms

from inventoryRequests.models import InventoryRequest, STATUS_CHOICES


class InventoryRequestForm(forms.ModelForm):
    requested_item = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    requested_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = InventoryRequest
        fields = '__all__'
