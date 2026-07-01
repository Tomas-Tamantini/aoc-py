from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.parser.csv_parser import parse_csv
from src.solutions.y2015.d02.logic.rectangular_box import RectangularBox


def parse_rectangular_boxes(
    input_reader: InputReader,
) -> Iterator[RectangularBox]:
    yield from parse_csv(
        input_reader,
        separator="x",
        mapper=lambda values: RectangularBox(*map(int, values)),
    )
