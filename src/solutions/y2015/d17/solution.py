from src.core.io_handler import IOHandler
from src.solutions.y2015.d17.logic.container_combination import (
    container_combinations,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 17

    containers = tuple(
        map(int, io_handler.input_reader(*prob_id).read_stripped_lines())
    )

    combinations = list(container_combinations(containers, 150))
    io_handler.write_result(*prob_id, part=1, result=len(combinations))

    combination_sizes = [len(combination) for combination in combinations]
    min_size = min(combination_sizes)
    num_smallest_combinations = sum(
        size == min_size for size in combination_sizes
    )
    io_handler.write_result(*prob_id, part=2, result=num_smallest_combinations)
