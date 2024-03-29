# Generated by Django 4.0.6 on 2022-07-11 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_itemordered'),
        ('myshop', '0004_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ordereditem',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.itemordered'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='item',
            order_with_respect_to='ordereditem',
        ),
    ]
