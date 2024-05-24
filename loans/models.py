from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()
