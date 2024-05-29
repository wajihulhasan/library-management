from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter a genre",
        error_messages={"invalid": "Enter a valid genre"},
    )
    description = models.TextField(
        help_text="Enter a description",
        error_messages={"invalid": "Enter a valid description"},
    )

    class Meta:
        verbose_name_plural = "Genres"
        verbose_name = "Genre"
        ordering = ["name"]
        unique_together = ("name", "description")

    def __str__(self):
        return self.name
