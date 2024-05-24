from django.db import models


# Create your models here.
class InventoryRequest(models.Model):
    requested_item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    requested_date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.requested_item
