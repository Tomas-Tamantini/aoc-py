from typing import Iterator

import pytest

from src.solutions.y2019.intcode.instruction_parser import (
    parse_intcode_instruction,
)
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


def _parse_param(param_str) -> IntcodeParameter:
    value = int(param_str[:-1])
    mode_chr = param_str[-1]
    mode = {
        "p": ParameterMode.POSITION,
        "i": ParameterMode.IMMEDIATE,
        "r": ParameterMode.RELATIVE,
    }[mode_chr]
    return IntcodeParameter(value=value, mode=mode)


def _parse_params(params_str) -> Iterator[IntcodeParameter]:
    return (_parse_param(part) for part in params_str.split())


@pytest.mark.parametrize(
    ("params", "expected"),
    [
        ([99], IntcodeHalt()),
        ([101, 2, 3, 4], IntcodeAdd(*_parse_params("2i 3p 4p"))),
        ([1002, 4, 3, 4], IntcodeMultiply(*_parse_params("4p 3i 4p"))),
        ([3, 50], IntcodeInput(*_parse_params("50p"))),
        ([104, 50], IntcodeOutput(*_parse_params("50i"))),
        ([105, 3, 4], IntcodeJumpIfTrue(*_parse_params("3i 4p"))),
        ([1106, 3, 4], IntcodeJumpIfFalse(*_parse_params("3i 4i"))),
        ([7, 2, 3, 4], IntcodeLessThan(*_parse_params("2p 3p 4p"))),
        ([10108, 2, 3, 4], IntcodeEquals(*_parse_params("2i 3p 4i"))),
        ([204, -34], IntcodeOutput(*_parse_params("-34r"))),
        ([109, 19], IntcodeRelativeBaseOffset(*_parse_params("19i"))),
    ],
)
def test_intcode_instruction_parser(params, expected):
    instruction = parse_intcode_instruction(*params)
    assert instruction == expected
