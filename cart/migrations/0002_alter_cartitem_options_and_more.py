# Generated by Django 4.0.6 on 2022-10-21 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Cart Item', 'verbose_name_plural': 'Cart Items'},
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='quality',
            new_name='quantity',
        ),
    ]
