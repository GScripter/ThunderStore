# Generated by Django 4.1.3 on 2023-01-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%Y/%m/%d'),
        ),
    ]
