from src.core.io_handler import IOHandler
from src.solutions.y2015.d24.logic.arrangements import (
    find_ideal_arrangement_qe,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 24

    reader = io_handler.input_reader(*prob_id)
    packages = [int(line) for line in reader.read_stripped_lines()]

    result_part1 = find_ideal_arrangement_qe(packages, num_groups=3)
    io_handler.write_result(*prob_id, part=1, result=result_part1)

    result_part2 = find_ideal_arrangement_qe(packages, num_groups=4)
    io_handler.write_result(*prob_id, part=2, result=result_part2)
