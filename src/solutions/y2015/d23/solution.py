from src.core.io_handler import IOHandler
from src.solutions.shared.vm import (
    Computer,
    Hardware,
    ImmutableProgram,
    Processor,
    Program,
)
from src.solutions.y2015.d23.logic.parse_collatz_instructions import (
    parse_collatz_instructions,
)


def _run_program(program: Program, register_a_value: int = 0) -> int:
    processor = Processor(register_values={"a": register_a_value})
    computer = Computer(hardware=Hardware(processor))
    computer.run(program)
    return processor.get_value_at_register(register="b")


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 23

    instructions = list(
        parse_collatz_instructions(io_handler.input_reader(*prob_id))
    )
    program = ImmutableProgram(instructions)

    result_p1 = _run_program(program)
    io_handler.write_result(*prob_id, part=1, result=result_p1)

    result_p2 = _run_program(program, register_a_value=1)
    io_handler.write_result(*prob_id, part=2, result=result_p2)
