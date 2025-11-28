from typing import Optional

from src.solutions.shared.vm.hardware import Hardware
from src.solutions.shared.vm.instruction import Instruction
from src.solutions.shared.vm.program import Program


class Computer:
    def __init__(self, hardware: Hardware):
        self._hardware = hardware

    def _next_instruction(self, program: Program) -> Optional[Instruction]:
        pc = self._hardware.processor.program_counter
        return program.get_instruction(pc)

    def run_next_instruction(self, program: Program) -> None:
        if instruction := self._next_instruction(program):
            instruction.execute(self._hardware)

    def run(self, program: Program) -> None:
        while instruction := self._next_instruction(program):
            instruction.execute(self._hardware)
