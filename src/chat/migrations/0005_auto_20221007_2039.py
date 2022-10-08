# Generated by Django 3.2.16 on 2022-10-08 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_auto_20221007_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='contact',
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
