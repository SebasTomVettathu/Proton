# Generated by Django 5.0.1 on 2024-03-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_delete_tbl_cpo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_watt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watt_data', models.CharField(max_length=50)),
            ],
        ),
    ]
