# Generated by Django 5.1.1 on 2024-12-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0025_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='img/d1.jpg', upload_to='profile_pictures/'),
        ),
    ]