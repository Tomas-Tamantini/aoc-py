from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d12.logic.packing import Region, Shape


def parse_shapes(input_reader: InputReader) -> Iterator[Shape]:
    current_id = 0
    cells = set()
    y = 0
    for line in input_reader.read_stripped_lines():
        if "#" in line or "." in line:
            cells.update(
                {Vector2D(x, y) for x, c in enumerate(line) if c == "#"}
            )
            y += 1
        elif cells:
            yield Shape(id=current_id, cells=cells)
            y = 0
            cells = set()
            current_id += 1


def _parse_packing_region(line: str) -> Region:
    parts = line.split(":")
    width, height = map(int, parts[0].split("x"))
    amounts = map(int, parts[-1].split())
    shape_requirements = {
        i: amount for i, amount in enumerate(amounts) if amount > 0
    }
    return Region(
        width=width, height=height, shape_requirements=shape_requirements
    )


def parse_packing_regions(input_reader: InputReader) -> Iterator[Region]:
    for line in input_reader.read_stripped_lines():
        if ":" in line and "x" in line:
            yield _parse_packing_region(line)
