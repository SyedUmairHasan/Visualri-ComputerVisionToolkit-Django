# Generated by Django 3.1.4 on 2021-01-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostream', '0004_video_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='neighbours',
        ),
        migrations.RemoveField(
            model_name='video',
            name='scale_factor',
        ),
        migrations.AddField(
            model_name='video',
            name='confidence',
            field=models.FloatField(default=0.3),
        ),
    ]
