# Generated by Django 5.0.2 on 2024-03-25 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_remove_billingdetails_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.billingdetails'),
        ),
    ]
