from functools import cache

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.intcode import (
    IntcodeProgram,
    SimpleSerialInput,
    SimpleSerialOutput,
    run_intcode_program,
)


class BeamSensor:
    def __init__(self, instructions: list[int]) -> None:
        self._instructions = instructions

    @cache
    def is_inside_beam(self, position: Vector2D) -> bool:
        program = IntcodeProgram(self._instructions)
        serial_input = SimpleSerialInput(input_values=[position.x, position.y])
        serial_output = SimpleSerialOutput()
        run_intcode_program(
            program, serial_input=serial_input, serial_output=serial_output
        )
        return bool(serial_output.last_output)
