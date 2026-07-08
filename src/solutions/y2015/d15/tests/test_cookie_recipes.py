from src.solutions.y2015.d15.logic.cookie_recipe import cookie_recipes
from src.solutions.y2015.d15.logic.ingredient import Ingredient


def test_all_cookie_recipes_are_yielded():
    ingredients = {
        Ingredient(
            capacity=-1, durability=-2, flavor=6, texture=3, calories=8
        ),
        Ingredient(
            capacity=2, durability=3, flavor=-2, texture=-1, calories=3
        ),
    }
    recipes = list(cookie_recipes(ingredients, total_teaspoons=100))
    assert max(cookie.score() for cookie in recipes) == 62842880
    assert (
        max(cookie.score() for cookie in recipes if cookie.calories() == 500)
        == 57600000
    )
