# Generated by Django 4.0.6 on 2022-07-11 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemOrdered',
        ),
    ]