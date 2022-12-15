from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import DateTimeField
from django.db.models.deletion import CASCADE

from colorfield.fields import ColorField

User = get_user_model()


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Тег',
        help_text='Введите тег',
    )
    color = ColorField(
        format='hex',
        max_length=7,
        unique=True,
        verbose_name='Цвет тега HEX',
        help_text='Введите цвет тега в HEX',
    )
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Слаг тега',
                            help_text='Здесь слаг тега',
                            )


class Ingredient(models.Model):
    """Модель ингредиента"""
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name='Ингредиент',
                            help_text='Введите ингредиент',
                            error_messages={'unique': 'Такой ингредиент уже существует'})
    measurement_unit = models.CharField(max_length=200,
                                        verbose_name='Единица измерения',
                                        help_text='Введите единицу измерения',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)


class Recipe(models.Model):
    """Модель рецепта"""
    name = models.CharField(max_length=200,
                            verbose_name='Название',
                            help_text='Введите название блюда',)
    author = models.ForeignKey(
        related_name='recipes',
        to=User,
        on_delete=CASCADE,
        verbose_name='Автор рецепта',
        help_text='Укажите автора рецепта'
    )
    text = models.TextField(
        verbose_name='Описание блюда',
        help_text='Введите описание блюда',)
    pub_date = DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    image = models.ImageField(
        upload_to='recipe_images/',
        blank=True,
        verbose_name='Фото блюда',
        help_text='Загрузите фото',)
    ingredients = models.ManyToManyField(
        to=Ingredient,
        through='IngredientContained',
        verbose_name='Ингредиенты',
        help_text='Перечислите ингредиенты',)
    tags = models.ManyToManyField(
        related_name='recipes',
        to=Tag,
        verbose_name='Теги',
        help_text='Здесь теги',)
    cooking_time = models.IntegerField(validators=[MinValueValidator(
            1, 'Количество должно превышать 0',
        )],
        verbose_name='Время приготовления',
        help_text='Укажите время приготовления',)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.text[:15]


class IngredientContained(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_contained',
        verbose_name='Ингредиент')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_contained',
        verbose_name='Рецепт')
    amount = models.IntegerField(
        validators=[MinValueValidator(
            1, 'Количество должно превышать 0',
        )],
        verbose_name='Количество'
    )

    def __str__(self):
        return (f'Ингредиент "{self.ingredient.name}"'
                f'в рецепте "{self.recipe.name}"')

    class Meta:
        verbose_name = 'Содержание ингредиента'
        verbose_name_plural = 'Содержание ингредиентов'
        constraints = (
            models.UniqueConstraint(
                fields=('ingredient', 'amount',),
                name='unique_ingredient_amount',
            ),
        )


class Favorite(models.Model):
    """Модель избранного контента"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite'
            )
        ]

    def __str__(self):
        return f'{self.user} {self.recipe}'


class ShoppingList(models.Model):
    """Модель списка покупок пользователя."""
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Подписчик на автора рецепта'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed',
        verbose_name='Автор',
        help_text='Автор рецепта'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['author', 'user'],
            name='unique_object'
        )]
