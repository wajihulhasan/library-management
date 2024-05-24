from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.book} - {self.patron} - {self.reservation_date}"
