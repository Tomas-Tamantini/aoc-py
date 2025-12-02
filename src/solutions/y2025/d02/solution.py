from src.core.io_handler import IOHandler
from src.solutions.y2025.d02.logic.invalid_ids import invalid_ids
from src.solutions.y2025.d02.logic.parser import parse_ranges


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 2

    ranges = list(parse_ranges(io_handler.input_reader(*prob_id)))

    sum_invalid_ids = sum(sum(invalid_ids(*r)) for r in ranges)

    io_handler.write_result(*prob_id, part=1, result=sum_invalid_ids)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
