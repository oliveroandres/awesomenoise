# Generated by Django 3.1.2 on 2020-11-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_video_clip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
