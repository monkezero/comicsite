# Generated by Django 5.1.1 on 2024-11-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0013_alter_product_apply_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='apply_discount',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]