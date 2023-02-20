# Generated by Django 4.1.6 on 2023-02-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheeltunes_app', '0002_alter_song_duration_alter_song_energy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='song',
            name='file',
        ),
        migrations.AddField(
            model_name='song',
            name='playable',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='static_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
