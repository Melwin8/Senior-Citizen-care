# Generated by Django 5.0.2 on 2024-03-25 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_billingdetails_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingdetails',
            name='order',
        ),
    ]
