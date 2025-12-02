from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.parser.csv_parser import parse_csv


def _parse_range(range_str: str) -> tuple[int, int]:
    return tuple(map(int, range_str.split("-")))


def parse_ranges(input_reader: InputReader) -> Iterator[tuple[int, int]]:
    for pair_str in next(parse_csv(input_reader)):
        yield _parse_range(pair_str)
