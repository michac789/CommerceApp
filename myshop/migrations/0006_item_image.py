# Generated by Django 4.0.6 on 2022-07-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_item_ordereditem_alter_item_order_with_respect_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
