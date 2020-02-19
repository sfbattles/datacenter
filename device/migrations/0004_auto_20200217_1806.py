# Generated by Django 3.0 on 2020-02-17 18:06

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20200217_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='data_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='device.DataCenter'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='device_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.fields.CharField, to='device.DeviceRole'),
        ),
    ]