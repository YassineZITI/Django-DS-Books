# Generated by Django 3.0 on 2022-05-20 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0002_auto_20220520_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='replay',
            name='likes',
        ),
        migrations.AddField(
            model_name='replay',
            name='likes',
            field=models.ManyToManyField(related_name='replay_like', to=settings.AUTH_USER_MODEL),
        ),
    ]