from typing import Protocol

from src.solutions.shared.vm.hardware import Hardware


class Instruction(Protocol):
    def execute(self, hardware: Hardware) -> None: ...
