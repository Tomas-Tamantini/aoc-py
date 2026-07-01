from src.core.io_handler import IOHandler
from src.solutions.y2015.d05.logic.ruleset import (
    first_ruleset,
    is_nice,
    second_ruleset,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 5
    strings = list(io_handler.input_reader(*prob_id).read_stripped_lines())

    num_nice_p1 = sum(is_nice(string, first_ruleset) for string in strings)
    io_handler.write_result(*prob_id, part=1, result=num_nice_p1)

    num_nice_p2 = sum(is_nice(string, second_ruleset) for string in strings)
    io_handler.write_result(*prob_id, part=2, result=num_nice_p2)
