from django.db import models
from positions.models import Position


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    hire_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
