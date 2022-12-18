# Generated by Django 2.2.19 on 2022-12-18 14:38

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Такой ингредиент уже существует'}, help_text='Введите ингредиент', max_length=200, unique=True, verbose_name='Ингредиент')),
                ('measurement_unit', models.CharField(help_text='Введите единицу измерения', max_length=200, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IngredientContained',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Количество должно превышать 0')], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Содержание ингредиента',
                'verbose_name_plural': 'Содержание ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название блюда', max_length=200, verbose_name='Название')),
                ('text', models.TextField(help_text='Введите описание блюда', verbose_name='Описание блюда')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, help_text='Загрузите фото', upload_to='recipe_images/', verbose_name='Фото блюда')),
                ('cooking_time', models.IntegerField(help_text='Укажите время приготовления', validators=[django.core.validators.MinValueValidator(1, 'Количество должно превышать 0')], verbose_name='Время приготовления')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите тег', max_length=30, unique=True, verbose_name='Тег')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Введите цвет тега в HEX', image_field=None, max_length=7, samples=None, unique=True, verbose_name='Цвет тега HEX')),
                ('slug', models.SlugField(help_text='Здесь слаг тега', max_length=200, unique=True, verbose_name='Слаг тега')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='recipes.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]
