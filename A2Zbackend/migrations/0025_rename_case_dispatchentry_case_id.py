# Generated by Django 4.2.3 on 2023-07-22 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0024_remove_company_id_alter_company_company_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispatchentry',
            old_name='case',
            new_name='case_id',
        ),
    ]
