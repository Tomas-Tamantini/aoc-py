from src.solutions.y2025.d01.logic.parser import parse_dial_instructions
from src.solutions.y2025.d01.logic.turn_dial import (
    DialInstruction,
    TurnDirection,
)


def test_parse_dial_instructions(input_reader):
    reader = input_reader(
        """
        L1
        R2
        L3
        R40
        """
    )
    instructions = list(parse_dial_instructions(reader))
    assert instructions == [
        DialInstruction(turn_direction=TurnDirection.LEFT, step_count=1),
        DialInstruction(turn_direction=TurnDirection.RIGHT, step_count=2),
        DialInstruction(turn_direction=TurnDirection.LEFT, step_count=3),
        DialInstruction(turn_direction=TurnDirection.RIGHT, step_count=40),
    ]
