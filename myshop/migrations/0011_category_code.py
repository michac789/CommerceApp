# Generated by Django 4.0.6 on 2022-07-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0010_item_closed_alter_item_buyer_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.CharField(default='', max_length=2, verbose_name='category_code'),
        ),
    ]
