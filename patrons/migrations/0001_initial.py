# Generated by Django 5.0.6 on 2024-05-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patron",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("membership_date", models.DateField()),
                ("membership_status", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]
