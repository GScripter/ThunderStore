# Generated by Django 4.1.3 on 2023-01-11 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]
