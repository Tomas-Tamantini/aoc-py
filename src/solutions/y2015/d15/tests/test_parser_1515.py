from src.solutions.y2015.d15.logic.ingredient import Ingredient
from src.solutions.y2015.d15.logic.parser import parse_ingredients


def test_parse_ingredients(input_reader):
    example = """
              Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
              Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
              """  # noqa: E501
    ingredients = list(parse_ingredients(input_reader(example)))
    assert ingredients == [
        Ingredient(
            capacity=-1, durability=-2, flavor=6, texture=3, calories=8
        ),
        Ingredient(
            capacity=2, durability=3, flavor=-2, texture=-1, calories=3
        ),
    ]
