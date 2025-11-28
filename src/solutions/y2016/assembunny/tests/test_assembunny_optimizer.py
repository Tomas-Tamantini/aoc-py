from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    NoOpInstruction,
    RegisterValue,
)
from src.solutions.y2016.assembunny.optimizer import optimize_assembunny_code


def test_optimize_addition():
    unoptimized = [
        IncrementInstruction(register="a"),
        DecrementInstruction(register="b"),
        JumpNotZeroInstruction(value=RegisterValue("b"), offset=-2),
    ]
    optimized = [
        IncrementInstruction(register="a", value=RegisterValue("b")),
        CopyInstruction(register="b", value=LiteralValue(0)),
        NoOpInstruction(),
    ]
    assert optimize_assembunny_code(unoptimized) == optimized
