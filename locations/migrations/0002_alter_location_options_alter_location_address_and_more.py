# Generated by Django 5.0.6 on 2024-05-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={
                "ordering": ["name"],
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
            },
        ),
        migrations.AlterField(
            model_name="location",
            name="address",
            field=models.CharField(
                error_messages={"unique": "Enter a unique Location Address"},
                help_text="Enter Location Address",
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="capacity",
            field=models.IntegerField(default=0, help_text="Enter Capacity"),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(
                error_messages={"unique": "Enter a unique Location Name"},
                help_text="Enter Location Name",
                max_length=100,
                unique=True,
            ),
        ),
    ]
