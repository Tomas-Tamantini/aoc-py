from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.number_theory.interval import Interval


def parse_intervals(input_reader: InputReader) -> Iterator[Interval]:
    for line in input_reader.read_stripped_lines():
        if "-" in line:
            yield Interval(*map(int, line.split("-")))


def parse_ingredient_ids(input_reader: InputReader) -> Iterator[int]:
    for line in input_reader.read_stripped_lines():
        if "-" not in line:
            yield int(line)
