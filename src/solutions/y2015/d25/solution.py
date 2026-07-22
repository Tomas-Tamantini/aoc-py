import re

from src.core.io_handler import IOHandler
from src.solutions.y2015.d25.logic.code_generator import get_code_at


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 25

    reader = io_handler.input_reader(*prob_id)
    line = reader.read_input()

    match = re.search(r"row (\d+), column (\d+)", line)
    if not match:
        raise ValueError("Invalid input format")

    row, col = map(int, match.groups())

    result = get_code_at(row, col)
    io_handler.write_result(*prob_id, part=1, result=result)
