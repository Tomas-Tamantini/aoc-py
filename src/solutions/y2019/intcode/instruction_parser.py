from typing import Iterable, Iterator

from src.core.input_reader import InputReader
from src.solutions.shared.vm import Instruction
from src.solutions.y2019.intcode.instructions import (
    IntcodeAdd,
    IntcodeEquals,
    IntcodeHalt,
    IntcodeInput,
    IntcodeJumpIfFalse,
    IntcodeJumpIfTrue,
    IntcodeLessThan,
    IntcodeMultiply,
    IntcodeOutput,
    IntcodeParameter,
    IntcodeRelativeBaseOffset,
    ParameterMode,
)


def parse_instructions(input_reader: InputReader) -> list[int]:
    return [int(code) for code in input_reader.read_input().split(",")]


def _parse_op_code(value: int) -> int:
    return value % 100


def _parse_modes(value: int, num_params: int) -> Iterator[ParameterMode]:
    value //= 100
    for _ in range(num_params):
        digit = value % 10
        value //= 10
        yield ParameterMode(digit)


def _parse_parameters(
    param_values: Iterable[int], modes: Iterable[ParameterMode]
) -> Iterator[IntcodeParameter]:
    return (
        IntcodeParameter(value=param_value, mode=mode)
        for mode, param_value in zip(modes, param_values)
    )


def parse_intcode_instruction(*params: int) -> Instruction:
    op_code = _parse_op_code(params[0])
    instructions = {
        1: (IntcodeAdd, 3),
        2: (IntcodeMultiply, 3),
        3: (IntcodeInput, 1),
        4: (IntcodeOutput, 1),
        5: (IntcodeJumpIfTrue, 2),
        6: (IntcodeJumpIfFalse, 2),
        7: (IntcodeLessThan, 3),
        8: (IntcodeEquals, 3),
        9: (IntcodeRelativeBaseOffset, 1),
        99: (IntcodeHalt, 0),
    }
    if op_code not in instructions:
        raise ValueError(f"Uknown op code {op_code}")
    instruction_cls, num_params = instructions[op_code]
    param_modes = _parse_modes(params[0], num_params)
    return instruction_cls(*_parse_parameters(params[1:], param_modes))
