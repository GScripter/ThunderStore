# Generated by Django 4.1.3 on 2022-12-21 18:45

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cpf',
            field=localflavor.br.models.BRCPFField(default=1, max_length=14, verbose_name='CPF'),
            preserve_default=False,
        ),
    ]
