# Generated by Django 4.2.3 on 2023-07-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0007_alter_vehicles_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]
