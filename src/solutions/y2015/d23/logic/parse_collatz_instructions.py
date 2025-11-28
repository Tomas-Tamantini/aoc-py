from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.vm import Instruction
from src.solutions.y2015.d23.logic.collatz_instructions import (
    CollatzHalveInstruction,
    CollatzIncrementInstruction,
    CollatzJumpIfEvenInstruction,
    CollatzJumpIfOneInstruction,
    CollatzJumpInstruction,
    CollatzTripleInstruction,
)


def _parse_collatz_instruction(line: str) -> Instruction:
    words = line.split()

    op_code = words[0]
    params = [p.replace(",", "").strip() for p in words[1:]]
    if op_code == "hlf":
        return CollatzHalveInstruction(register=params[0])
    elif op_code == "tpl":
        return CollatzTripleInstruction(register=params[0])
    elif op_code == "inc":
        return CollatzIncrementInstruction(register=params[0])
    elif op_code == "jmp":
        return CollatzJumpInstruction(offset=int(params[-1]))
    elif op_code == "jie":
        return CollatzJumpIfEvenInstruction(
            register=params[0], offset=int(params[-1])
        )
    elif op_code == "jio":
        return CollatzJumpIfOneInstruction(
            register=params[0], offset=int(params[-1])
        )
    else:
        raise ValueError("Could not parse instruction")


def parse_collatz_instructions(
    input_reader: InputReader,
) -> Iterator[Instruction]:
    for line in input_reader.read_stripped_lines():
        yield _parse_collatz_instruction(line)
