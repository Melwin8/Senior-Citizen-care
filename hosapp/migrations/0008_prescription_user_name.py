# Generated by Django 5.0.2 on 2024-03-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0007_prescription_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
