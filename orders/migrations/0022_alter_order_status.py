# Generated by Django 4.0.6 on 2022-12-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=50),
        ),
    ]
