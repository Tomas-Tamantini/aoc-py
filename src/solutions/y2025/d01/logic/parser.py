from typing import Iterator

from src.core.input_reader import InputReader


def _parse_dial_offset(instruction: str) -> int:
    offset = int(instruction[1:])
    if instruction[0] == "L":
        return -offset
    else:
        return offset


def parse_dial_offsets(input_reader: InputReader) -> Iterator[int]:
    for line in input_reader.read_stripped_lines():
        yield _parse_dial_offset(line)
