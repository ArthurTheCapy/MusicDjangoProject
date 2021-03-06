# Generated by Django 4.0.4 on 2022-07-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_album_cover_alter_album_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musicapp.album'),
            preserve_default=False,
        ),
    ]
