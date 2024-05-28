from django.db import models


# Create your models here.
class InventoryRequest(models.Model):
    requested_item = models.CharField(max_length=255,help_text="Enter the name of the item")
    quantity = models.PositiveIntegerField(help_text="How many items do you have?")
    requested_date = models.DateField(help_text="Enter the date of request")
    status = models.CharField(max_length=255,help_text="Enter the status of the request")

    class Meta:
        verbose_name_plural = "Inventory Requests"
        verbose_name = "Inventory Request"


    def __str__(self):
        return self.requested_item
