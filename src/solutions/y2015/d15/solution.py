from src.core.io_handler import IOHandler
from src.solutions.y2015.d15.logic.cookie_recipe import cookie_recipes
from src.solutions.y2015.d15.logic.parser import parse_ingredients


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 15

    ingredients = set(parse_ingredients(io_handler.input_reader(*prob_id)))
    recipes = cookie_recipes(ingredients, total_teaspoons=100)
    max_score_1 = max_score_2 = 0
    for cookie in recipes:
        score = cookie.score()
        max_score_1 = max(max_score_1, score)
        if cookie.calories() == 500:
            max_score_2 = max(max_score_2, score)
    io_handler.write_result(*prob_id, part=1, result=max_score_1)
    io_handler.write_result(*prob_id, part=2, result=max_score_2)
