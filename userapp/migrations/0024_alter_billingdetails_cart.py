# Generated by Django 5.0.2 on 2024-03-27 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_remove_cartitem_billing_details_billingdetails_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.cartitem'),
        ),
    ]
