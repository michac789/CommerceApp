# Generated by Django 4.0.6 on 2022-07-12 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0013_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='joined_data',
            new_name='joined_time',
        ),
    ]
