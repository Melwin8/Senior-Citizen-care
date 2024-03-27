# Generated by Django 5.0.2 on 2024-03-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0009_remove_profiledb_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxibooking',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
