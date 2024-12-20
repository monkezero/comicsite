# Generated by Django 5.1.1 on 2024-12-19 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0033_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xsite.product')),
            ],
        ),
    ]
