# Generated by Django 2.2.19 on 2022-12-20 07:04

import django.core.validators
from django.db import migrations

import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20221219_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=7, samples=None, unique=True, validators=[django.core.validators.RegexValidator(message='Проверьте вводимый формат', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='HEX-код'),
        ),
    ]
