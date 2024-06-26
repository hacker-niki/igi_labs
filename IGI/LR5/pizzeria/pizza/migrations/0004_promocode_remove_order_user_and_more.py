# Generated by Django 5.0.6 on 2024-05-22 14:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pizza', '0003_alter_pizza_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sale_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='image',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='client_orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='courier_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='category',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Courier',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
