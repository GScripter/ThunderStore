# Generated by Django 4.1.3 on 2023-01-01 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='Product',
            new_name='product',
        ),
    ]