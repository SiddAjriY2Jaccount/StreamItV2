# Generated by Django 2.1.2 on 2018-10-20 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_songdetails_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='songdetails',
            name='songid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='music.Songs'),
        ),
    ]
