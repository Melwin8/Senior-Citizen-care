# Generated by Django 5.0.2 on 2024-03-01 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_delete_contactdb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegistrationDb',
        ),
    ]
