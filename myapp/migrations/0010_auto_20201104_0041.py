# Generated by Django 3.1.2 on 2020-11-04 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20201104_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albume',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-id']},
        ),
    ]