# Generated by Django 4.0.6 on 2022-12-06 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_image',
        ),
    ]