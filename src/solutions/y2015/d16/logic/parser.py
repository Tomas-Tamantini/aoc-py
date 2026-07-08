from typing import Iterator

from src.core.io_handler import InputReader
from src.solutions.y2015.d16.logic.aunt import Aunt


def _parse_aunt(line: str) -> Aunt:
    parts = line.split(": ", 1)
    aunt_id = int(parts[0].split(" ")[1])
    attributes = parts[1].split(", ")
    attr_dict = {
        attr.split(": ")[0]: int(attr.split(": ")[1]) for attr in attributes
    }
    return Aunt(id=aunt_id, attributes=attr_dict)


def parse_aunts(reader: InputReader) -> Iterator[Aunt]:
    for line in reader.read_stripped_lines():
        yield _parse_aunt(line)
