from dataclasses import dataclass

from src.core.io_handler import IOHandler
from src.solutions.y2019.d21.logic.parse_springscript import parse_springscript
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    SimpleSerialInput,
    SimpleSerialOutput,
    parse_instructions,
    run_intcode_program,
)


@dataclass(frozen=True)
class _SpringbotResult:
    hull_damage: int = 0
    last_moments: str = ""


def _parse_output_values(output_values: list[int]) -> _SpringbotResult:
    if output_values[-1] > 255:
        return _SpringbotResult(hull_damage=output_values[-1])
    else:
        return _SpringbotResult(
            last_moments="".join(chr(i) for i in output_values)
        )


def _run_springscript_program(
    intcode_instructions: list[int], input_values: list[int]
) -> _SpringbotResult:
    serial_input = SimpleSerialInput(input_values)
    serial_output = SimpleSerialOutput()
    program = IntcodeProgram(intcode_instructions)
    run_intcode_program(program, serial_input, serial_output)
    return _parse_output_values(serial_output.output_values)


def _solve(
    io_handler: IOHandler, intcode_instructions: list[int], part: int
) -> int:
    prob_id = 2019, 21
    file_name = f"solution_part_{part}.txt"
    reader = io_handler.input_reader(*prob_id, file_name=file_name)
    input_values = list(parse_springscript(reader))
    result = _run_springscript_program(intcode_instructions, input_values)
    if result.last_moments:
        print(result.last_moments)
    return result.hull_damage


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 21

    intcode_instructions = parse_instructions(
        input_reader=io_handler.input_reader(*prob_id)
    )

    for part in (1, 2):
        result = _solve(io_handler, intcode_instructions, part)
        io_handler.write_result(*prob_id, part=part, result=result)
