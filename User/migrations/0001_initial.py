# Generated by Django 4.2.7 on 2024-04-07 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CPO', '0004_remove_tbl_chargingport_district'),
        ('Guest', '0010_delete_tbl_chargingport'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('booking_fordate', models.DateField()),
                ('booking_fortime', models.TimeField()),
                ('booking_amount', models.CharField(max_length=10)),
                ('booking_status', models.CharField(default=0, max_length=20)),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPO.tbl_chargingport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
