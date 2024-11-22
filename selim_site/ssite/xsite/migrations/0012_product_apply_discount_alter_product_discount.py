# Generated by Django 5.1.1 on 2024-11-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0011_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='apply_discount',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
