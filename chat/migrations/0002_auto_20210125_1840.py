# Generated by Django 3.1.3 on 2021-01-25 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210115_2344'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.AddField(
            model_name='message',
            name='author1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author1_messages', to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='message',
            name='author2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author2_messages', to='accounts.profile'),
        ),
    ]