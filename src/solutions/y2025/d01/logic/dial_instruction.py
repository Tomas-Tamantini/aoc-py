from dataclasses import dataclass
from enum import Enum


class TurnDirection(Enum):
    LEFT = "L"
    RIGHT = "R"


@dataclass(frozen=True)
class DialInstruction:
    turn_direction: TurnDirection
    step_count: int
