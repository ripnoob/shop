# Generated by Django 4.0.6 on 2022-12-06 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200)),
                ('profile_image', models.ImageField(blank=True, upload_to='photos/user/profile')),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]