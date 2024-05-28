from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100, help_text="Enter your name")
    contact_info = models.CharField(max_length=100,help_text="Enter your contact info")

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ['name']
        unique_together = (('name', 'contact_info'),)

    def __str__(self):
        return self.name
