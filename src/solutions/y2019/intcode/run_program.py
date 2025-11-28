from typing import Optional

from src.solutions.shared.vm import (
    Computer,
    Hardware,
    Processor,
    SerialInput,
    SerialOutput,
)
from src.solutions.y2019.intcode.program import IntcodeProgram


def run_intcode_program(
    program: IntcodeProgram,
    serial_input: Optional[SerialInput] = None,
    serial_output: Optional[SerialOutput] = None,
) -> None:
    computer = Computer(
        Hardware(
            processor=Processor(),
            memory=program,
            serial_input=serial_input,
            serial_output=serial_output,
        )
    )
    computer.run(program)
