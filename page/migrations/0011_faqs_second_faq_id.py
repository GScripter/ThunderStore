# Generated by Django 4.1.3 on 2023-01-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_faqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqs',
            name='second_faq_id',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
