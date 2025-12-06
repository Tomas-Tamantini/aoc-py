from src.solutions.y2025.d06.logic.parser import parse_math_problems
from src.core.io_handler import IOHandler


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 6

    reader = io_handler.input_reader(*prob_id)

    problems = parse_math_problems(reader)
    total = sum(p.evaluate() for p in problems)
    io_handler.write_result(*prob_id, part=1, result=total)

    io_handler.write_result(*prob_id, part=2, result="not implemented")
