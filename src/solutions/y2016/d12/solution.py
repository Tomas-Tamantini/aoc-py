from src.core.io_handler import IOHandler
from src.solutions.shared.vm.computer import Computer
from src.solutions.shared.vm.hardware import Hardware
from src.solutions.shared.vm.processor import Processor
from src.solutions.shared.vm.program import ImmutableProgram, Program
from src.solutions.y2016.assembunny.optimizer import optimize_assembunny_code
from src.solutions.y2016.assembunny.parser import parse_assembunny_instructions


def _run_program(processor: Processor, program: Program) -> None:
    computer = Computer(Hardware(processor))
    computer.run(program)


def solve(io_handler: IOHandler) -> None:
    prob_id = 2016, 12
    instructions = list(
        parse_assembunny_instructions(io_handler.input_reader(*prob_id))
    )
    program = ImmutableProgram(optimize_assembunny_code(instructions))

    processor = Processor()
    _run_program(processor, program)
    value_at_a = processor.get_value_at_register("a")
    io_handler.write_result(*prob_id, part=1, result=value_at_a)

    processor = Processor(register_values={"c": 1})
    _run_program(processor, program)
    value_at_a = processor.get_value_at_register("a")
    io_handler.write_result(*prob_id, part=2, result=value_at_a)
