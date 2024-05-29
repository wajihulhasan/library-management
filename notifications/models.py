from django.db import models

from patrons.models import Patron


# Create your models here.
class Notification(models.Model):
    message = models.TextField(help_text="The message to be displayed")
    date = models.DateTimeField(auto_now_add=True)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("date", "patron"),)
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ["-date"]

    def __str__(self):
        return self.message
