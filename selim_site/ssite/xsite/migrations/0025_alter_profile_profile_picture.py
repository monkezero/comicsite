# Generated by Django 5.1.1 on 2024-12-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsite', '0024_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/'),
        ),
    ]