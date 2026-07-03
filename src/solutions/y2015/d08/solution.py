from src.core.io_handler import IOHandler
from src.solutions.y2015.d08.logic.string_encoding import (
    encoded_length,
    memory_length,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 8

    lines = list(io_handler.input_reader(*prob_id).read_stripped_lines())

    part1 = sum(len(line) - memory_length(line) for line in lines)
    io_handler.write_result(*prob_id, part=1, result=part1)

    part2 = sum(encoded_length(line) - len(line) for line in lines)
    io_handler.write_result(*prob_id, part=2, result=part2)
