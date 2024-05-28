from django.db import models

from books.models import Book
from patrons.models import Patron


# Create your models here.
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    review_text = models.TextField(help_text="Enter your review text",error_messages={'required':'Please enter your review text',})
    rating = models.IntegerField(default=0,help_text="Enter your rating")
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('book', 'patron')
    def __str__(self):
        return self.review_text
