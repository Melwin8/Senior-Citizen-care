# Generated by Django 5.0.2 on 2024-03-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_age', models.IntegerField()),
                ('patient_gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]