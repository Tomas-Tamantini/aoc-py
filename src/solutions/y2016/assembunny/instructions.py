from dataclasses import dataclass
from typing import Hashable, Optional, Protocol

from src.solutions.shared.vm import Hardware


class RegisterOrLiteral(Protocol):
    def get_value(self, hardware: Hardware) -> int: ...


@dataclass(frozen=True)
class LiteralValue(RegisterOrLiteral):
    value: int

    def get_value(self, hardware: Hardware) -> int:
        return self.value


@dataclass(frozen=True)
class RegisterValue(RegisterOrLiteral):
    register: Hashable

    def get_value(self, hardware: Hardware) -> int:
        return hardware.processor.get_value_at_register(self.register)


@dataclass(frozen=True)
class NoOpInstruction:
    @staticmethod
    def execute(hardware: Hardware) -> None:
        hardware.processor.increment_program_counter()


@dataclass(frozen=True)
class IncrementInstruction:
    register: Hashable
    value: Optional[RegisterOrLiteral] = None

    def execute(self, hardware: Hardware) -> None:
        increment = self.value.get_value(hardware) if self.value else 1
        old_value = hardware.processor.get_value_at_register(self.register)
        hardware.processor.set_value_at_register(
            self.register, old_value + increment
        )
        hardware.processor.increment_program_counter()


@dataclass(frozen=True)
class DecrementInstruction:
    register: Hashable

    def execute(self, hardware: Hardware) -> None:
        old_value = hardware.processor.get_value_at_register(self.register)
        hardware.processor.set_value_at_register(self.register, old_value - 1)
        hardware.processor.increment_program_counter()


@dataclass(frozen=True)
class CopyInstruction:
    register: Hashable
    value: RegisterOrLiteral

    def execute(self, hardware: Hardware) -> None:
        value = self.value.get_value(hardware)
        hardware.processor.set_value_at_register(self.register, value)
        hardware.processor.increment_program_counter()


@dataclass(frozen=True)
class JumpNotZeroInstruction:
    value: RegisterOrLiteral
    offset: int

    def execute(self, hardware: Hardware) -> None:
        if self.value.get_value(hardware) == 0:
            hardware.processor.increment_program_counter()
        else:
            hardware.processor.increment_program_counter(self.offset)
