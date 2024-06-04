
from django import forms

from staffSchedules.models import StaffSchedule


class StaffScheduleForm(forms.ModelForm):
    class Meta:
        model = StaffSchedule
        fields = '__all__'
