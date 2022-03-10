# Generated by Django 3.1.3 on 2021-01-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_choice', models.CharField(choices=[('1', 'Camera'), ('2', 'IP Webcam')], max_length=50)),
                ('scale_factor', models.FloatField(default=1.3)),
                ('neighbours', models.IntegerField(default=5)),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
    ]
