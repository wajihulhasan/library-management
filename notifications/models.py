from django.db import models

from patrons.models import Patron


# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
