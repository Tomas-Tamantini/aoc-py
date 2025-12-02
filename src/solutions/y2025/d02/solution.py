from src.core.io_handler import IOHandler
from src.solutions.y2025.d02.logic.invalid_ids import invalid_ids
from src.solutions.y2025.d02.logic.parser import parse_ranges


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 2

    ranges = list(parse_ranges(io_handler.input_reader(*prob_id)))

    total_p1 = sum(sum(invalid_ids(*r, multiplicity=2)) for r in ranges)
    io_handler.write_result(*prob_id, part=1, result=total_p1)

    total_p2 = sum(sum(invalid_ids(*r, multiplicity=None)) for r in ranges)
    io_handler.write_result(*prob_id, part=2, result=total_p2)
