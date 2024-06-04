from django.db import models

from books.models import Book
from supplier.models import Supplier


# Create your models here.
class BookOrder(models.Model):
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("R", "Received"),
        ("C", "Cancelled"),
        ("F", "Fulfilled"),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1, help_text="Quantity of order will be one by default"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")

    class Meta:
        ordering = ["order_date"]
        unique_together = (("book", "supplier"),)

    def __str__(self):
        return f"{self.supplier} {self.book} {self.quantity} {self.order_date}"
