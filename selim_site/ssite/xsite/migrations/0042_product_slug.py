# Generated by Django 5.1.1 on 2025-01-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0041_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
