# Generated by Django 4.1 on 2023-01-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_remove_add_to_cart_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_to_cart',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]