# Generated by Django 4.1 on 2023-01-18 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcatagory',
            name='sub_catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcatagory', to='product.catagory'),
        ),
    ]
