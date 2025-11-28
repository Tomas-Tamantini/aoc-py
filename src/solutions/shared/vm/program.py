from typing import Iterable, Optional, Protocol

from src.solutions.shared.vm.instruction import Instruction


class Program(Protocol):
    def get_instruction(
        self, program_counter: int
    ) -> Optional[Instruction]: ...


class ImmutableProgram:
    def __init__(self, instructions: Iterable[Instruction]):
        self._instructions = tuple(instructions)

    def get_instruction(self, program_counter: int) -> Optional[Instruction]:
        if 0 <= program_counter < len(self._instructions):
            return self._instructions[program_counter]
