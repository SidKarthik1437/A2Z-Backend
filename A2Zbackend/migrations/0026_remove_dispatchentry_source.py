# Generated by Django 4.2.3 on 2023-07-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0025_rename_case_dispatchentry_case_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatchentry',
            name='source',
        ),
    ]
