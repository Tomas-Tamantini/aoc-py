from dataclasses import dataclass
from enum import Enum
from typing import Iterator


@dataclass(frozen=True)
class TurnDial:
    num_positions: int
    start_position: int


class TurnDirection(Enum):
    LEFT = "L"
    RIGHT = "R"


@dataclass(frozen=True)
class DialInstruction:
    turn_direction: TurnDirection
    step_count: int

    @property
    def offset(self) -> int:
        return (
            self.step_count
            if self.turn_direction == TurnDirection.RIGHT
            else -self.step_count
        )


def dial_positions(
    dial: TurnDial, instructions: list[DialInstruction]
) -> Iterator[int]:
    pos = dial.start_position
    yield pos
    for instruction in instructions:
        pos = (pos + instruction.offset) % dial.num_positions
        yield pos
