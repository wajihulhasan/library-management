from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the publisher",error_messages={'required': "The name must be provided"})
    address = models.CharField(max_length=255, help_text="The address of the publisher")
    contact = models.CharField(max_length=255, help_text="The contact number of the publisher")

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ['name']
        unique_together = (('name', 'contact'),)

    def __str__(self):
        return self.name
