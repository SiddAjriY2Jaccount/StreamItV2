# Generated by Django 2.1.2 on 2018-10-24 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_auto_20181024_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdetails',
            name='songid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='music.Songs'),
        ),
    ]