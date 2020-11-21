# Generated by Django 3.1.2 on 2020-11-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20201104_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='albume',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], default='ACTIVE', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='albume',
            name='link',
            field=models.CharField(default='Copy link Here', max_length=100, null=True),
        ),
    ]
