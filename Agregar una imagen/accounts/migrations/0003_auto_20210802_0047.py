# Generated by Django 3.2 on 2021-08-02 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
