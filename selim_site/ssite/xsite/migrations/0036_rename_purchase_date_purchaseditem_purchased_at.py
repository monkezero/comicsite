# Generated by Django 5.1.1 on 2024-12-19 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0035_purchaseditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseditem',
            old_name='purchase_date',
            new_name='purchased_at',
        ),
    ]
