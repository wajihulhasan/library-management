from django.db import models

from locations.models import Location


# Create your models here.
class Event(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Event title",
        error_messages={"max_length": "Event title must be less than 256 characters"},
    )
    description = models.TextField(help_text="Event description")
    start_date = models.DateField(help_text="Event start date")
    date = models.DateField(help_text="Event date")
    time = models.TimeField(help_text="Event time")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]
        verbose_name = "Event"
        verbose_name_plural = "Events"
        unique_together = (("date", "location"),)

    def __str__(self):
        return self.title
