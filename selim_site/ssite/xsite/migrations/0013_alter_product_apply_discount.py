# Generated by Django 5.1.1 on 2024-11-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0012_product_apply_discount_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='apply_discount',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
    ]