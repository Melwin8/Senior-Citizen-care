# Generated by Django 5.0.2 on 2024-03-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0010_taxibooking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxibooking',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]