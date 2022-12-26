# Generated by Django 4.1.3 on 2022-12-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_remove_item_is_sent_order_is_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cep',
            field=models.CharField(max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
    ]
