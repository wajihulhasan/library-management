from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    loan_date = models.DateField(help_text="Date of loan")
    due_date = models.DateField(help_text="Date of due")
    return_date = models.DateField(help_text="Date of return")

    class Meta:
        unique_together = (("book", "patron"),)
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        ordering = ["return_date"]

    def __str__(self):
        return f"{self.return_date} - {self.book.title}"
