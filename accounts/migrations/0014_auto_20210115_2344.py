# Generated by Django 3.1.3 on 2021-01-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210115_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static/avatar.png', upload_to='avatars/'),
        ),
    ]