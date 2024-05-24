from django.db import models

from events.models import Event
from patrons.models import Patron


# Create your models here.
class eventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
