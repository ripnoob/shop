# Generated by Django 4.0.6 on 2022-12-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='New', max_length=50),
        ),
    ]
