# Generated by Django 4.0.6 on 2022-10-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='is_active',
            new_name='is_available',
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('Color', 'Color'), ('Size', 'Size')], max_length=200),
        ),
    ]
