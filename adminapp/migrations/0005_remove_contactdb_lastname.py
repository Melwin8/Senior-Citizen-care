# Generated by Django 5.0.2 on 2024-03-12 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_driverregistrationdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdb',
            name='LastName',
        ),
    ]
