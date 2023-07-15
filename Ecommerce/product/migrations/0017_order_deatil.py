# Generated by Django 4.1 on 2023-01-27 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_cotact_number_address_contact_number'),
        ('product', '0016_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_deatil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('product_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.add_to_cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]