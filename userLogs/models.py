from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()

    class Meta:
        unique_together = (('user', 'date'),)
        verbose_name = 'User Logs'
        verbose_name_plural = 'User Logs'
        ordering = ['-date']
        get_latest_by = 'date'


    def __str__(self):
        return self.date
