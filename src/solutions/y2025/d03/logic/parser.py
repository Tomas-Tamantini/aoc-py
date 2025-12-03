from typing import Iterator

from src.core.input_reader import InputReader


def parse_battery_banks(
    input_reader: InputReader,
) -> Iterator[tuple[int, ...]]:
    for line in input_reader.read_stripped_lines():
        yield tuple(int(digit) for digit in line)
