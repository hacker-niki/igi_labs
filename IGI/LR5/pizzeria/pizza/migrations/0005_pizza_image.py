# Generated by Django 5.0.6 on 2024-05-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_promocode_remove_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(default=0, upload_to='media/pizza/'),
            preserve_default=False,
        ),
    ]
