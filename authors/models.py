from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name
