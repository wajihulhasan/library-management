from django.db import models

from books.models import Book


# Create your models here.
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    acquisition_date = models.DateField(
        help_text='Please select date of acquisition of the book',
        error_messages={
            "empty": "date is required",
            "invalid": "Please enter a valid date",
        }
    )
    condition = models.TextField()

    class Meta:
        unique_together = (("book", "acquisition_date"),)
