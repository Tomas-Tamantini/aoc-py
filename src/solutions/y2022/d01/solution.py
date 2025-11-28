from src.core.io_handler import IOHandler
from src.solutions.y2022.d01.logic.parser import parse_calories


def solve(io_handler: IOHandler) -> None:
    prob_id = 2022, 1
    calories_by_elf = [
        sum(calories)
        for calories in parse_calories(io_handler.input_reader(*prob_id))
    ]
    sorted_calories = sorted(calories_by_elf)

    max_calories = sorted_calories[-1]
    io_handler.write_result(*prob_id, part=1, result=max_calories)

    top_three_calories = sum(sorted_calories[-3:])
    io_handler.write_result(*prob_id, part=2, result=top_three_calories)
