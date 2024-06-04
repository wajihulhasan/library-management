from django.db import models

from loans.models import Loan

FINE_STATUS_CHOICES = [
    ('UNPAID', 'Unpaid'),
    ('PAID', 'Paid'),
    ('WAIVED', 'Waived'),
]
# Create your models here.
class Fine(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(help_text="Amount of loan", default=0)
    reason = models.TextField(help_text="Reason for loan", default="")
    status = models.CharField(
        max_length=10,
        choices=FINE_STATUS_CHOICES,
        default='UNPAID',
        help_text="Status of the fine"
    )

    class Meta:
        ordering = ["loan", "amount"]
        unique_together = ("loan", "amount")

    def __str__(self):
        return f"{self.loan.loan_date} - {self.amount}"
