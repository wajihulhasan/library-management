from django.db import models

# Create your models here.


class Patron(models.Model):
    name = models.CharField(max_length=100, help_text="Name of patron")
    email = models.EmailField(
        help_text="Email of patron",
        unique=True,
        error_messages={"unique": "A patron with this email already exists."},
    )
    membership_date = models.DateField(help_text="Date of membership")
    membership_status = models.CharField(max_length=100, help_text="Status of patron")
    address = models.CharField(max_length=100, help_text="Address of patron")

    class Meta:
        verbose_name = "patron"
        verbose_name_plural = "patrons"
        unique_together = (("name", "email"),)

    def __str__(self):
        return self.name
