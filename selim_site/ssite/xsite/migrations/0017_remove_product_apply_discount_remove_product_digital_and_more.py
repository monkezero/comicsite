# Generated by Django 5.1.1 on 2024-11-22 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0016_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='apply_discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subname',
        ),
    ]
