# Generated by Django 4.1 on 2023-01-15 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_address_cotact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='cotact_number',
            new_name='contact_number',
        ),
    ]
