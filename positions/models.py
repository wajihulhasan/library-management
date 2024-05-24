from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=100)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def __str__(self):
        return self.title
