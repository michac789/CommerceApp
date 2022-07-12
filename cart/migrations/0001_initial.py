# Generated by Django 4.0.6 on 2022-07-11 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshop', '0009_alter_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oncart', to='myshop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oncart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]