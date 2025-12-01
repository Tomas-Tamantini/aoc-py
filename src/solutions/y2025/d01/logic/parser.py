from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d01.logic.turn_dial import (
    DialInstruction,
    TurnDirection,
)


def parse_dial_instruction(instruction: str) -> DialInstruction:
    turn_direction = TurnDirection(instruction[0])
    return DialInstruction(turn_direction, int(instruction[1:]))


def parse_dial_instructions(
    input_reader: InputReader,
) -> Iterator[DialInstruction]:
    for line in input_reader.read_stripped_lines():
        yield parse_dial_instruction(line)
