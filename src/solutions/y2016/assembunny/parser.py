from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.vm import Instruction
from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    RegisterOrLiteral,
    RegisterValue,
)


def _parse_literal_or_register(argument: str) -> RegisterOrLiteral:
    try:
        return LiteralValue(int(argument))
    except ValueError:
        return RegisterValue(argument)


def _parse_assembunny_instruction(line: str) -> Instruction:
    op_code, *args = line.split()
    return {
        "inc": lambda args: IncrementInstruction(register=args[0]),
        "dec": lambda args: DecrementInstruction(register=args[0]),
        "cpy": lambda args: CopyInstruction(
            value=_parse_literal_or_register(args[0]), register=args[1]
        ),
        "jnz": lambda args: JumpNotZeroInstruction(
            value=_parse_literal_or_register(args[0]), offset=int(args[1])
        ),
    }[op_code](args)


def parse_assembunny_instructions(
    input_reader: InputReader,
) -> Iterator[Instruction]:
    for line in input_reader.read_stripped_lines():
        yield _parse_assembunny_instruction(line)
