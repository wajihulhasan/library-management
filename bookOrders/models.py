from django.db import models

from books.models import Book
from supplier.models import Supplier


# Create your models here.
class bookOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.supplier} {self.book} {self.quantity} {self.order_date}'
