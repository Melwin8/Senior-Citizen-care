# Generated by Django 5.0.2 on 2024-03-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_userregistrationdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalRegistrationDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospitalname', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]