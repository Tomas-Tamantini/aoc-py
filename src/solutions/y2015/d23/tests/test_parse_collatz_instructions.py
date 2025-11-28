from src.solutions.y2015.d23.logic.collatz_instructions import (
    CollatzHalveInstruction,
    CollatzIncrementInstruction,
    CollatzJumpIfEvenInstruction,
    CollatzJumpIfOneInstruction,
    CollatzJumpInstruction,
    CollatzTripleInstruction,
)
from src.solutions.y2015.d23.logic.parse_collatz_instructions import (
    parse_collatz_instructions,
)


def test_collatz_instructions_are_properly_parsed(input_reader):
    reader = input_reader(
        """
        hlf a
        tpl b
        inc c
        jmp +3
        jie d, -42
        jio e, 123
        """
    )
    instructions = list(parse_collatz_instructions(reader))
    assert instructions == [
        CollatzHalveInstruction(register="a"),
        CollatzTripleInstruction(register="b"),
        CollatzIncrementInstruction(register="c"),
        CollatzJumpInstruction(offset=3),
        CollatzJumpIfEvenInstruction(register="d", offset=-42),
        CollatzJumpIfOneInstruction(register="e", offset=123),
    ]
