# Generated by Django 4.1 on 2023-01-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_catagory_subcatagory_product_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcatagory',
            name='sub_catagory_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
