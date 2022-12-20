from collections import Counter

from recipe.models import IngredientContained


def get_shopping_cart(user):
    ingredients = IngredientContained.objects.filter(
        recipe__shop_list__user=user.user
    )
    compressed_ingredients = Counter()
    for ing in ingredients:
        compressed_ingredients[
            (ing.ingredient.name, ing.ingredient.measurement_unit)
        ] += ing.amount
    return ([
        f"- {name}: {amount} {measurement_unit}\n"
        for (name, measurement_unit), amount
        in compressed_ingredients.items()
    ])