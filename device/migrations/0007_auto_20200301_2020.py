# Generated by Django 3.0 on 2020-03-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_auto_20200301_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='port',
            old_name='switch',
            new_name='switch_id',
        ),
    ]
