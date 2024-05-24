# Generated by Django 5.0.6 on 2024-05-24 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('patrons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('patron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrons.patron')),
            ],
        ),
    ]
