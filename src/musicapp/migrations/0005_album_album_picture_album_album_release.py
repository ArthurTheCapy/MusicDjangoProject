# Generated by Django 4.0.4 on 2022-06-21 20:32

from django.db import migrations, models
import django.utils.timezone
import musicapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_remove_album_release_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_release',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]