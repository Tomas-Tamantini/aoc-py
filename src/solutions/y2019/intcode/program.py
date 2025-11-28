from typing import Optional

from src.solutions.shared.vm import Instruction
from src.solutions.y2019.intcode.instruction_parser import (
    parse_intcode_instruction,
)


class IntcodeProgram:
    def __init__(self, instructions: list[int]) -> None:
        self._instructions = {
            addr: value for addr, value in enumerate(instructions)
        }

    def read(self, address: int) -> int:
        if address < 0:
            raise ValueError("Cannot access negative address")
        return self._instructions.get(address, 0)

    def write(self, address: int, value: int) -> None:
        self._instructions[address] = value

    def get_instruction(self, program_counter: int) -> Optional[Instruction]:
        if program_counter < 0:
            return None
        else:
            return parse_intcode_instruction(
                *(
                    self._instructions.get(program_counter + i, 0)
                    for i in range(4)
                )
            )
