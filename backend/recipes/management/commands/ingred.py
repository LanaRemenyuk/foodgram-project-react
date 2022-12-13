import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Импорт ингредиентов в базу данных"

    def handle(self, **kwargs):
        with open(
            # f"{settings.BASE_DIR}\\ingredients.csv",
            f"D:\\foodgram-project-react\\data\\ingredients.csv",
            "r",
            encoding="UTF-8"
        ) as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                Ingredient.objects.get_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
        self.stdout.write(
            self.style.SUCCESS("***Ingredients were succesfully loaded***")
        )