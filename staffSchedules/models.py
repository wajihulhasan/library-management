from django.db import models

from employees.models import Employee


# Create your models here.
class StaffSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.TimeField(help_text='Enter start time')
    end_time = models.TimeField(help_text='Enter end time')
    days = models.IntegerField(help_text='Enter number of days')

    class Meta:
        unique_together = (('employee', 'start_time', 'end_time'),)
        verbose_name = 'Staff Schedule'
        verbose_name_plural = 'Staff Schedule'


    def __str__(self):
        return str(self.employee)
