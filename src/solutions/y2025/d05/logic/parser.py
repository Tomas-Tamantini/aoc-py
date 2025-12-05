from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d05.logic.number_range import NumberRange


def parse_number_ranges(input_reader: InputReader) -> Iterator[NumberRange]:
    for line in input_reader.read_stripped_lines():
        if "-" in line:
            yield NumberRange(*map(int, line.split("-")))


def parse_ingredient_ids(input_reader: InputReader) -> Iterator[int]:
    for line in input_reader.read_stripped_lines():
        if "-" not in line:
            yield int(line)
