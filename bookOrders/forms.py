from django import forms

from bookOrders.models import BookOrder


class BookOrderForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    order_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    widgets = {
        "status": forms.Select(attrs={"class": "form-control"}),
    }

    class Meta:
        model = BookOrder
        fields = "__all__"
