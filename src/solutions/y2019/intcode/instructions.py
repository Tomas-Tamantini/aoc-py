from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from src.solutions.shared.vm.hardware import Hardware

RELATIVE_BASE_REGISTER = -1


class ParameterMode(int, Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


@dataclass(frozen=True)
class IntcodeParameter:
    value: int
    mode: ParameterMode

    def evaluate(self, hardware: Hardware) -> int:
        if self.mode == ParameterMode.IMMEDIATE:
            return self.value
        else:
            return hardware.memory.read(address=self.address(hardware))

    def address(self, hardware: Hardware) -> int:
        if self.mode == ParameterMode.POSITION:
            return self.value
        elif self.mode == ParameterMode.RELATIVE:
            return self.value + hardware.processor.get_value_at_register(
                RELATIVE_BASE_REGISTER
            )
        else:
            raise ValueError("Cannot extract address from immediate mode")


@dataclass(frozen=True)
class IntcodeHalt:
    @staticmethod
    def execute(hardware: Hardware) -> None:
        hardware.processor.set_program_counter(-1)


@dataclass(frozen=True)
class _BinaryOperation(ABC):
    input_a: IntcodeParameter
    input_b: IntcodeParameter
    output: IntcodeParameter

    @staticmethod
    @abstractmethod
    def _operate(a: int, b: int) -> int: ...

    def execute(self, hardware: Hardware) -> None:
        a = self.input_a.evaluate(hardware)
        b = self.input_b.evaluate(hardware)
        result = self._operate(a, b)
        address = self.output.address(hardware)
        hardware.memory.write(address=address, value=result)
        hardware.processor.increment_program_counter(increment=4)


@dataclass(frozen=True)
class IntcodeAdd(_BinaryOperation):
    @staticmethod
    def _operate(a: int, b: int) -> int:
        return a + b


@dataclass(frozen=True)
class IntcodeMultiply(_BinaryOperation):
    @staticmethod
    def _operate(a: int, b: int) -> int:
        return a * b


@dataclass(frozen=True)
class IntcodeLessThan(_BinaryOperation):
    @staticmethod
    def _operate(a: int, b: int) -> int:
        return int(a < b)


@dataclass(frozen=True)
class IntcodeEquals(_BinaryOperation):
    @staticmethod
    def _operate(a: int, b: int) -> int:
        return int(a == b)


@dataclass(frozen=True)
class IntcodeInput:
    store_at: IntcodeParameter

    def execute(self, hardware: Hardware) -> None:
        input_value = hardware.serial_input.read_next()
        address = self.store_at.address(hardware)
        hardware.memory.write(address=address, value=input_value)
        hardware.processor.increment_program_counter(increment=2)


@dataclass(frozen=True)
class IntcodeOutput:
    source: IntcodeParameter

    def execute(self, hardware: Hardware) -> None:
        output_value = self.source.evaluate(hardware)
        hardware.serial_output.put(output_value)
        hardware.processor.increment_program_counter(increment=2)


@dataclass(frozen=True)
class _JumpOperation(ABC):
    value: IntcodeParameter
    jump_to: IntcodeParameter

    @staticmethod
    @abstractmethod
    def _condition_is_met(evaluation: int) -> bool: ...

    def execute(self, hardware: Hardware) -> None:
        if self._condition_is_met(self.value.evaluate(hardware)):
            jump_address = self.jump_to.evaluate(hardware)
            hardware.processor.set_program_counter(jump_address)
        else:
            hardware.processor.increment_program_counter(increment=3)


@dataclass(frozen=True)
class IntcodeJumpIfTrue(_JumpOperation):
    @staticmethod
    def _condition_is_met(evaluation: int) -> bool:
        return evaluation != 0


@dataclass(frozen=True)
class IntcodeJumpIfFalse(_JumpOperation):
    @staticmethod
    def _condition_is_met(evaluation: int) -> bool:
        return evaluation == 0


@dataclass(frozen=True)
class IntcodeRelativeBaseOffset:
    offset: IntcodeParameter

    def execute(self, hardware: Hardware) -> None:
        reg = RELATIVE_BASE_REGISTER
        increment = self.offset.evaluate(hardware)
        previous = hardware.processor.get_value_at_register(reg)
        new_value = previous + increment
        hardware.processor.set_value_at_register(register=reg, value=new_value)
        hardware.processor.increment_program_counter(increment=2)
