# Generated by Django 4.1.6 on 2023-02-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheeltunes_app', '0004_alter_song_energy_alter_song_playable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='mood',
            field=models.CharField(default='middle', max_length=100),
        ),
    ]
