from src.core.io_handler import IOHandler
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    SimpleSerialInput,
    SimpleSerialOutput,
    parse_instructions,
    run_intcode_program,
)


def _run_program(instructions: list[int], input_value: int) -> int:
    program = IntcodeProgram(instructions)
    serial_output = SimpleSerialOutput()
    run_intcode_program(
        program,
        serial_output=serial_output,
        serial_input=SimpleSerialInput(input_values=[input_value]),
    )
    return serial_output.last_output


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 9
    instructions = parse_instructions(io_handler.input_reader(*prob_id))

    result = _run_program(instructions, input_value=1)
    io_handler.write_result(*prob_id, part=1, result=result)

    result = _run_program(instructions, input_value=2)
    io_handler.write_result(*prob_id, part=2, result=result)
