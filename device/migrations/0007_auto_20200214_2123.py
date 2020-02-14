# Generated by Django 3.0 on 2020-02-14 21:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_auto_20200214_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switch',
            old_name='switch_label',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='switchport',
            old_name='port',
            new_name='port_number',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='device_description',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='device_hostname',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='patch_port',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='switch_port',
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_description', models.CharField(blank=True, max_length=250, null=True)),
                ('device_hostname', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='device.DeviceHostName')),
                ('patch_port', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.PatchPort')),
                ('switch_port', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.SwitchPort')),
            ],
            options={
                'verbose_name': 'Port',
                'verbose_name_plural': 'Port',
                'db_table': 'Port',
            },
        ),
        migrations.AddField(
            model_name='switch',
            name='port_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device.Port'),
            preserve_default=False,
        ),
    ]
