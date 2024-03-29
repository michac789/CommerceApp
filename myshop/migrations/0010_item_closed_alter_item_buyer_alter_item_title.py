# Generated by Django 4.0.6 on 2022-07-11 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshop', '0009_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='buyer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_bought', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
