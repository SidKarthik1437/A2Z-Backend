# Generated by Django 4.2.3 on 2023-07-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0026_remove_dispatchentry_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchstatus',
            name='dispatch_status_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
