# Generated by Django 4.0.5 on 2022-07-01 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_album_cover_alter_album_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='label',
        ),
    ]
