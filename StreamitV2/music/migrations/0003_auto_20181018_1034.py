# Generated by Django 2.1.2 on 2018-10-18 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_songplays'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songhits', models.IntegerField()),
                ('is_favourite', models.BooleanField(default=False)),
                ('songid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Songs')),
            ],
        ),
        migrations.RemoveField(
            model_name='songplays',
            name='songid',
        ),
        migrations.DeleteModel(
            name='SongPlays',
        ),
    ]
