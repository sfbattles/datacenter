# Generated by Django 3.0 on 2020-02-17 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switch',
            old_name='port_id',
            new_name='port',
        ),
    ]
