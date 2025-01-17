# Generated by Django 5.1.1 on 2024-11-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0009_delete_contact_product_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='subname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
