from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Department Name",
        error_messages={"unique": "A department with that name already exists"},
    )
    description = models.TextField()

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return self.name
