# Generated by Django 5.0.1 on 2024-04-06 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPO', '0002_remove_tbl_chargingport_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_chargingport',
            name='port_id',
        ),
    ]