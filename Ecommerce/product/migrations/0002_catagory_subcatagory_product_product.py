# Generated by Django 4.1 on 2023-01-13 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(choices=[('Mens', 'Mens'), ('Womens', 'Womens'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Medicine', 'Medicine')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.catagory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.subcatagory'),
            preserve_default=False,
        ),
    ]
