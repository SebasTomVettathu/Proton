# Generated by Django 5.0.1 on 2024-01-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
                ('admin_email', models.EmailField(max_length=254, unique=True)),
                ('admin_contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='tbl_brand',
        ),
        migrations.DeleteModel(
            name='tbl_catagory',
        ),
    ]