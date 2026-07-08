from dataclasses import dataclass
from itertools import combinations
from typing import Iterator

from src.solutions.y2015.d15.logic.ingredient import Ingredient


@dataclass(frozen=True)
class Cookie:
    ingredients: dict[Ingredient, int]

    def score(self) -> int:
        total_score = 1
        for attribute in ["capacity", "durability", "flavor", "texture"]:
            attribute_sum = sum(
                getattr(ingredient, attribute) * teaspoons
                for ingredient, teaspoons in self.ingredients.items()
            )
            total_score *= max(attribute_sum, 0)
        return total_score

    def calories(self) -> int:
        return sum(
            ingredient.calories * teaspoons
            for ingredient, teaspoons in self.ingredients.items()
        )


def _generate_partitions(n: int, total: int) -> Iterator[list[int]]:
    num_dividers = n - 1
    num_total = total + num_dividers
    for dividers in combinations(range(num_total), num_dividers):
        partition = []
        last_divider = -1
        for divider in dividers:
            partition.append(divider - last_divider - 1)
            last_divider = divider
        partition.append(num_total - last_divider - 1)
        yield partition


def cookie_recipes(
    ingredients: set[Ingredient], total_teaspoons: int
) -> Iterator[Cookie]:
    num_ingredients = len(ingredients)
    for partition in _generate_partitions(num_ingredients, total_teaspoons):
        yield Cookie(dict(zip(ingredients, partition)))
