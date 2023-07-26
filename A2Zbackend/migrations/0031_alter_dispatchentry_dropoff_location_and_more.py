# Generated by Django 4.2.3 on 2023-07-22 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0030_alter_dispatchentry_asset_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchentry',
            name='dropoff_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dispatchentryassets',
            name='colorid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dispatchentryassets',
            name='dispatch_entry_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchentry'),
        ),
    ]