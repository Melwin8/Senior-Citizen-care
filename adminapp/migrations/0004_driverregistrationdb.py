# Generated by Django 5.0.2 on 2024-03-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_hospitalregistrationdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverRegistrationDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drivername', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
