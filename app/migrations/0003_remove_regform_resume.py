# Generated by Django 4.1.3 on 2023-04-06 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_adregisterform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regform',
            name='resume',
        ),
    ]
