from typing import Iterator

from src.core.io_handler import IOHandler


def _floors(instructions: str) -> Iterator[int]:
    floor = 0
    yield floor
    for c in instructions:
        offset = 1 if c == "(" else -1
        floor += offset
        yield floor


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 1
    instructions = io_handler.input_reader(*prob_id).read_input().strip()

    floors = list(_floors(instructions))

    io_handler.write_result(*prob_id, part=1, result=floors[-1])
    io_handler.write_result(*prob_id, part=2, result=floors.index(-1))
