from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    reservation_date = models.DateField(help_text="Date of reservation")
    expiry_date = models.DateField(help_text="Date of expiration")

    class Meta:
        unique_together = (("book", "patron"),)
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ["book", "patron"]

    def __str__(self):
        return f"{self.book} - {self.patron} - {self.reservation_date}"
