from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.date
