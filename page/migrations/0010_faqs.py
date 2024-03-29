# Generated by Django 4.1.3 on 2023-01-28 04:44

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_politicpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('faq_id', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
