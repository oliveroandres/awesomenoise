# Generated by Django 3.1.2 on 2020-11-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
