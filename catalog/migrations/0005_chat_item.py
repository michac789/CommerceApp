# Generated by Django 4.0.6 on 2022-07-11 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_alter_category_id'),
        ('catalog', '0004_chat_chatcontent_remove_reply_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='myshop.item'),
        ),
    ]