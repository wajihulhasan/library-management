
from django import forms

from employees.models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class': 'form-control'}))
    class Meta:
        model = Employee
        fields = '__all__'
