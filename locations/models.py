from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter Location Name",
        unique=True,
        error_messages={"unique": "Enter a unique Location Name"},
    )
    address = models.CharField(
        max_length=100,
        help_text="Enter Location Address",
        unique=True,
        error_messages={"unique": "Enter a unique Location Address"},
    )
    capacity = models.IntegerField(help_text="Enter Capacity", default=0)
    type = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name
