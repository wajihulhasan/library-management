from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron =models.ForeignKey(Patron, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.review_text