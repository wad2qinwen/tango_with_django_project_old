# Generated by Django 2.2.17 on 2023-01-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
