from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=100, unique=True, help_text="Title of the position",error_messages={'unique': 'A position with that title already exists.'})
    responsibility = models.CharField(max_length=100,help_text="Responsibility of the position")
    min_salary = models.IntegerField(help_text="Minimum salary")
    max_salary = models.IntegerField(help_text="Maximum salary")

    class Meta:
        ordering = ['title']
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.title
