from src.core.io_handler import IOHandler
from src.solutions.y2018.d14.logic.hot_chocolate import (
    HotChocolateRecipeScores,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2018, 14
    num_steps = int(io_handler.input_reader(*prob_id).read_input())
    recipe_scores = HotChocolateRecipeScores(first_score=3, second_score=7)
    score_generator = recipe_scores.generate_scores()

    first_scores = [next(score_generator) for _ in range(num_steps + 10)]
    last_ten_scores = "".join(
        map(str, first_scores[num_steps : num_steps + 10])
    )
    io_handler.write_result(*prob_id, part=1, result=last_ten_scores)
    io_handler.progress_monitor(*prob_id, part=2).estimate_remaining_time(
        estimation="20s"
    )
    first_occurrence = recipe_scores.first_occurrence_of_subsequence(
        tuple(map(int, str(num_steps)))
    )
    io_handler.write_result(*prob_id, part=2, result=first_occurrence)
