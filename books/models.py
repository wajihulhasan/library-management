from django.db import models

from authors.models import Author
from genres.models import Genre
from publishers.models import Publisher


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, help_text="Title of book",error_messages={'required': 'Title is required'})
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_date = models.DateField(help_text="Date of publishing",error_messages={'required': 'Date of publishing is required'})
    quantity_available = models.PositiveSmallIntegerField(default=0, help_text="Quantity of book available",error_messages={'required': 'Quantity of book is required'})
    isbn = models.CharField("ISBN", max_length=13,help_text="ISBN of book")
    genre = models.ManyToManyField(Genre, blank=True,help_text="Genre of book")

    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        unique_together = (('title', 'author'),)
