# Generated by Django 5.1.6 on 2025-03-01 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='customertype',
            table='customer_type',
        ),
    ]
