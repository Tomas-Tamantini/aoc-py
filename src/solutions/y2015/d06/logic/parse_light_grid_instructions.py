from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2015.d06.logic.light_grid import (
    DecreaseBrightnessInstruction,
    IncreaseBrightnessInstruction,
    LightGridInstruction,
    ToggleInstruction,
    TurnOffInstruction,
    TurnOnInstruction,
)


def _parse_coords(coords: str) -> Vector2D:
    x, y = coords.split(",")
    return Vector2D(int(x), int(y))


def _parse_instruction(
    line: str, translate_instructions: bool
) -> LightGridInstruction:
    if line.startswith("turn on "):
        rest = line[len("turn on ") :]
        start_str, _, end_str = rest.split()
    elif line.startswith("turn off "):
        rest = line[len("turn off ") :]
        start_str, _, end_str = rest.split()
    elif line.startswith("toggle "):
        rest = line[len("toggle ") :]
        start_str, _, end_str = rest.split()
    else:
        raise ValueError(f"Unknown instruction: {line}")

    region = BoundingBox([_parse_coords(start_str), _parse_coords(end_str)])

    if translate_instructions:
        if line.startswith("turn on"):
            return IncreaseBrightnessInstruction(region, increase_amount=1)
        elif line.startswith("turn off"):
            return DecreaseBrightnessInstruction(region)
        else:
            return IncreaseBrightnessInstruction(region, increase_amount=2)
    elif line.startswith("turn on"):
        return TurnOnInstruction(region)
    elif line.startswith("turn off"):
        return TurnOffInstruction(region)
    else:
        return ToggleInstruction(region)


def parse_light_grid_instructions(
    input_reader: InputReader, translate_instructions: bool = False
) -> Iterator[LightGridInstruction]:
    for line in input_reader.read_stripped_lines():
        yield _parse_instruction(line, translate_instructions)
