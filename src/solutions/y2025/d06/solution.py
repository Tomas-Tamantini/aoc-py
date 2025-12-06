from src.core.io_handler import IOHandler
from src.solutions.y2025.d06.logic.parser import (
    parse_math_problems_by_column,
    parse_math_problems_by_row,
)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 6

    reader = io_handler.input_reader(*prob_id)

    problems_p1 = parse_math_problems_by_row(reader)
    total_p1 = sum(p.evaluate() for p in problems_p1)
    io_handler.write_result(*prob_id, part=1, result=total_p1)

    problems_p2 = parse_math_problems_by_column(reader)
    total_p2 = sum(p.evaluate() for p in problems_p2)
    io_handler.write_result(*prob_id, part=2, result=total_p2)
