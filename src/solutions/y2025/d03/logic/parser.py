from typing import Iterator

from src.core.input_reader import InputReader


def _parse_battery_bank(battery_bank: str) -> Iterator[int]:
    for digit in battery_bank:
        yield int(digit)


def parse_battery_banks(
    input_reader: InputReader,
) -> Iterator[tuple[int, ...]]:
    for line in input_reader.read_stripped_lines():
        yield tuple(_parse_battery_bank(line))
