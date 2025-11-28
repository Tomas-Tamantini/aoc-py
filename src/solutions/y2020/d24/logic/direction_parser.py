from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.geometry import HexagonalDirection


def _parse_hexagonal_directions_from_line(
    line: str,
) -> Iterator[HexagonalDirection]:
    matches = {
        "e": HexagonalDirection.EAST,
        "w": HexagonalDirection.WEST,
        "se": HexagonalDirection.SOUTHEAST,
        "sw": HexagonalDirection.SOUTHWEST,
        "ne": HexagonalDirection.NORTHEAST,
        "nw": HexagonalDirection.NORTHWEST,
    }
    pointer = 0
    while pointer < len(line):
        if line[pointer] in matches:
            yield matches[line[pointer]]
            pointer += 1
        else:
            yield matches[line[pointer : pointer + 2]]
            pointer += 2


def parse_hexagonal_directions(
    input_reader: InputReader,
) -> Iterator[list[HexagonalDirection]]:
    for line in input_reader.read_stripped_lines():
        yield list(_parse_hexagonal_directions_from_line(line))
