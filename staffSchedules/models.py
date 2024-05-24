from django.db import models

from employees.models import Employee


# Create your models here.
class staffSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.IntegerField()

    def __str__(self):
        return str(self.employee)
