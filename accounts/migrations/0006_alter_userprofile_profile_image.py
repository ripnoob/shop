# Generated by Django 4.0.6 on 2022-12-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='photos/default/default_user.png', upload_to='photos/user/profile'),
        ),
    ]
