# Generated by Django 4.0.4 on 2022-06-23 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_album_album_picture_album_album_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='musiclabel',
            old_name='label_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='musiclabel',
            old_name='label_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='playlist',
            old_name='playlist_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_release',
        ),
        migrations.RemoveField(
            model_name='track',
            name='author',
        ),
        migrations.AddField(
            model_name='album',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.musiclabel'),
        ),
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(default='2022-06-23'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.PositiveSmallIntegerField(),
        ),
    ]