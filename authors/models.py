from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Please Enter the full name of the author",
        error_messages={
            "blank": "This field is required.",
            "max_length": "The name is too long. It should be 255 characters or less.",
        },
    )
    bio = models.TextField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
