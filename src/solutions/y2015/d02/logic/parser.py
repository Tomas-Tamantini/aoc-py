from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2015.d02.logic.rectangular_box import RectangularBox


def _parse_rectangular_box(line: str) -> RectangularBox:
    return RectangularBox(*map(int, line.split("x")))


def parse_rectangular_boxes(
    input_reader: InputReader,
) -> Iterator[RectangularBox]:
    for line in input_reader.read_stripped_lines():
        yield _parse_rectangular_box(line)
