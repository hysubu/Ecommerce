# Generated by Django 4.1 on 2023-01-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_order_deatil_product_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_deatil',
            name='total_price',
            field=models.CharField(max_length=100),
        ),
    ]
