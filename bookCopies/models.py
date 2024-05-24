from django.db import models

from books.models import Book


# Create your models here.
class bookCopies(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    acquisition_date = models.DateField()
    condition = models.TextField()
