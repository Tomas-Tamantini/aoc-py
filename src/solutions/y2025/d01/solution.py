from typing import Iterator

from src.core.io_handler import IOHandler
from src.solutions.y2025.d01.logic.parser import parse_dial_offsets


def _absolute_positions(
    dial_start_pos: int, offsets: list[int]
) -> Iterator[int]:
    pos = dial_start_pos
    yield pos
    for offset in offsets:
        pos += offset
        yield pos


def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 1

    offsets = list(parse_dial_offsets(io_handler.input_reader(*prob_id)))

    dial_start_pos = 50
    dial_size = 100

    positions = list(_absolute_positions(dial_start_pos, offsets))

    num_zeros = len([p for p in positions if p % dial_size == 0])

    io_handler.write_result(*prob_id, part=1, result=num_zeros)
    io_handler.write_result(*prob_id, part=2, result="not implemented")
