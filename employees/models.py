from django.db import models
from positions.models import Position


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Name of employee")
    email = models.EmailField(help_text="Email of employee", unique=True)
    hire_date = models.DateField(help_text="Date of hire of employee")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        unique_together = (("email", "position"),)

    def __str__(self):
        return self.name
