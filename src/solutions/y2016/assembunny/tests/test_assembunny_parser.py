from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    RegisterValue,
)
from src.solutions.y2016.assembunny.parser import parse_assembunny_instructions


def test_assembunny_parser_parses_instructions(input_reader):
    reader = input_reader("""cpy 41 a
                             cpy b c
                             inc a
                             dec b
                             jnz a 2
                             jnz 1 5
                             """)
    instructions = list(parse_assembunny_instructions(reader))
    assert instructions == [
        CopyInstruction(register="a", value=LiteralValue(41)),
        CopyInstruction(register="c", value=RegisterValue("b")),
        IncrementInstruction(register="a"),
        DecrementInstruction(register="b"),
        JumpNotZeroInstruction(value=RegisterValue("a"), offset=2),
        JumpNotZeroInstruction(value=LiteralValue(1), offset=5),
    ]
