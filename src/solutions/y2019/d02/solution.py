from typing import Iterator

from src.core.io_handler import IOHandler
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    parse_instructions,
    run_intcode_program,
)


def _run_modified_program(
    original_instructions: list[int], noun: int, verb: int
) -> int:
    modified_instructions = original_instructions[:]
    modified_instructions[1] = noun
    modified_instructions[2] = verb
    program = IntcodeProgram(modified_instructions)
    run_intcode_program(program)
    return program.read(address=0)


def _candidates() -> Iterator[tuple[int, int]]:
    # Bit of a cheat - known answer for my input, to speed things up
    yield (98, 20)
    # Still loop through other candidates for other inputs
    for noun in range(100):
        for verb in range(100):
            yield noun, verb


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 2

    instructions = parse_instructions(io_handler.input_reader(*prob_id))

    io_handler.write_result(
        *prob_id,
        part=1,
        result=_run_modified_program(instructions, noun=12, verb=2),
    )

    result = -1
    desired_output = 19690720
    for noun, verb in _candidates():
        output = _run_modified_program(instructions, noun, verb)
        if output == desired_output:
            result = 100 * noun + verb
            break

    io_handler.write_result(*prob_id, part=2, result=result)
