# Generated by Django 4.1.3 on 2023-02-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('file', models.FileField(upload_to='')),
                ('energy', models.IntegerField(blank=True, null=True)),
                ('tempo', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]