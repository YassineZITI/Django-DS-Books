# Generated by Django 3.0 on 2022-06-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220528_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(),
        ),
    ]
