# Generated by Django 3.0 on 2020-02-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_portspeed_porttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortSpeedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'PortSpeedType',
                'verbose_name_plural': 'PortSpeedTypes',
                'db_table': 'PortSpeedType',
            },
        ),
    ]
