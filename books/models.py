from django.db import models

from authors.models import Author
from genres.models import Genre
from publishers.models import Publisher


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_date = models.DateField()
    quantity_available = models.PositiveSmallIntegerField(default=0)
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, blank=True)

