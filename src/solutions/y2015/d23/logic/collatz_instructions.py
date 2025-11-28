from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.solutions.shared.vm import Hardware


@dataclass(frozen=True)
class _NonJumpCollatzInstruction(ABC):
    register: str

    @staticmethod
    @abstractmethod
    def _update_value(current_value: int) -> int: ...

    def execute(self, hardware: Hardware) -> None:
        current_value = hardware.processor.get_value_at_register(self.register)
        new_value = self._update_value(current_value)
        hardware.processor.set_value_at_register(self.register, new_value)
        hardware.processor.increment_program_counter()


@dataclass(frozen=True)
class CollatzHalveInstruction(_NonJumpCollatzInstruction):
    @staticmethod
    def _update_value(current_value: int) -> int:
        return current_value // 2


@dataclass(frozen=True)
class CollatzTripleInstruction(_NonJumpCollatzInstruction):
    @staticmethod
    def _update_value(current_value: int) -> int:
        return current_value * 3


@dataclass(frozen=True)
class CollatzIncrementInstruction(_NonJumpCollatzInstruction):
    @staticmethod
    def _update_value(current_value: int) -> int:
        return current_value + 1


@dataclass(frozen=True)
class _CollatzJumpInstruction(ABC):
    offset: int

    @abstractmethod
    def _condition_is_met(self, hardware: Hardware) -> bool: ...

    def execute(self, hardware: Hardware) -> None:
        offset = self.offset if self._condition_is_met(hardware) else 1
        hardware.processor.increment_program_counter(offset)


@dataclass(frozen=True)
class CollatzJumpInstruction(_CollatzJumpInstruction):
    def _condition_is_met(self, hardware: Hardware) -> bool:  # noqa: PLR6301
        return True


@dataclass(frozen=True)
class CollatzJumpIfEvenInstruction(_CollatzJumpInstruction):
    register: str

    def _condition_is_met(self, hardware: Hardware) -> bool:
        register_value = hardware.processor.get_value_at_register(
            self.register
        )
        return register_value % 2 == 0


@dataclass(frozen=True)
class CollatzJumpIfOneInstruction(_CollatzJumpInstruction):
    register: str

    def _condition_is_met(self, hardware: Hardware) -> bool:
        register_value = hardware.processor.get_value_at_register(
            self.register
        )
        return register_value == 1
