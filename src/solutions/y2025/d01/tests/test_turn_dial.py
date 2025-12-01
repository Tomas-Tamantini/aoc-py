from src.solutions.y2025.d01.logic.turn_dial import (
    DialInstruction,
    TurnDial,
    TurnDirection,
    dial_positions,
)


def test_turn_dial_uses_modular_arithmetic():
    dial = TurnDial(num_positions=100, start_position=50)
    instructions = [
        DialInstruction(TurnDirection.RIGHT, step_count=21),
        DialInstruction(TurnDirection.RIGHT, step_count=35),
        DialInstruction(TurnDirection.LEFT, step_count=20),
    ]
    positions = list(dial_positions(dial, instructions))
    assert positions == [50, 71, 6, 86]
