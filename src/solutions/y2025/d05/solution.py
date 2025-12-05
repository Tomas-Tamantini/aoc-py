from src.core.io_handler import IOHandler
from src.solutions.y2025.d05.logic.parser import (
    parse_ingredient_ids,
    parse_number_ranges,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 5

    reader = io_handler.input_reader(*prob_id)

    ranges = list(parse_number_ranges(reader))
    ids = list(parse_ingredient_ids(reader))

    total = sum(any(r.contains(id) for r in ranges) for id in ids)

    io_handler.write_result(*prob_id, part=1, result=total)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
