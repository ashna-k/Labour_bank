# Generated by Django 4.1.3 on 2023-03-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adregisterform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afname', models.CharField(max_length=225)),
                ('alname', models.CharField(max_length=225)),
                ('aemail', models.CharField(max_length=225)),
                ('passwd', models.CharField(max_length=225)),
                ('cpasswd', models.CharField(max_length=225)),
            ],
        ),
    ]
