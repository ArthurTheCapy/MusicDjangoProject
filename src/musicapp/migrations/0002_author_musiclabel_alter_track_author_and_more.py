# Generated by Django 4.0.4 on 2022-06-20 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('band_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MusicLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=100)),
                ('label_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='track',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.author')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.track')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.author')),
            ],
        ),
    ]
