# Generated by Django 4.1 on 2023-01-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcatagory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
