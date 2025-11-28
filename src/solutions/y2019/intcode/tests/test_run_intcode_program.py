import pytest

from src.solutions.y2019.intcode.program import IntcodeProgram
from src.solutions.y2019.intcode.run_program import run_intcode_program
from src.solutions.y2019.intcode.serial_io import (
    SimpleSerialInput,
    SimpleSerialOutput,
)


@pytest.mark.parametrize(
    ("instructions", "final_state_diff"),
    [
        ((1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50), {0: 3500, 3: 70}),
        ((1, 0, 0, 0, 99), {0: 2}),
        ((2, 3, 0, 3, 99), {3: 6}),
        ((2, 4, 4, 5, 99, 0), {5: 9801}),
        ((1, 1, 1, 4, 99, 5, 6, 0, 99), {0: 30, 4: 2}),
    ],
)
def test_run_no_jump_intcode_program(instructions, final_state_diff):
    program = IntcodeProgram(instructions)
    run_intcode_program(program)
    final_state = [
        final_state_diff.get(i, inst) for i, inst in enumerate(instructions)
    ]
    assert all(
        program.read(address=i) == final_state[i]
        for i in range(len(instructions))
    )


@pytest.mark.parametrize(
    ("input_value", "expected_output"), [(7, 999), (8, 1000), (9, 1001)]
)
def test_branching_intcode_program(input_value, expected_output):
    raw_instructions = (
        "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
        "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
        "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    )
    program = IntcodeProgram(
        instructions=list(map(int, raw_instructions.split(",")))
    )
    serial_input = SimpleSerialInput(input_values=[input_value])
    serial_output = SimpleSerialOutput()
    run_intcode_program(
        program, serial_input=serial_input, serial_output=serial_output
    )
    assert serial_output.last_output == expected_output


def test_relative_base_quine_program():
    raw_instructions = (
        "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    )
    instructions = list(map(int, raw_instructions.split(",")))
    program = IntcodeProgram(instructions)
    serial_output = SimpleSerialOutput()
    run_intcode_program(program, serial_output=serial_output)
    assert serial_output.output_values == instructions
