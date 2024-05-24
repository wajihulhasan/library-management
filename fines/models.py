from django.db import models

from loans.models import Loan


# Create your models here.
class Fine(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.BooleanField(default=False)
