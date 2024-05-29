from django.db import models

from events.models import Event
from patrons.models import Patron


# Create your models here.
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(
        auto_now_add=True, help_text="Date of registration"
    )

    class Meta:
        unique_together = (("event", "patron"),)
        verbose_name = "Event Registration"
        verbose_name_plural = "Event Registrations"

    def __str__(self):
        return f"{self.event.title} - {self.patron.name}"
