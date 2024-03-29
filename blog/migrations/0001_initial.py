# Generated by Django 4.1.3 on 2023-01-02 23:38

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='blog/%Y/%m/%d')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
