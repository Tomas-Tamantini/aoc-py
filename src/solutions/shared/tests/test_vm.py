from dataclasses import dataclass
from typing import Hashable

import pytest

from src.solutions.shared.vm import (
    Computer,
    Hardware,
    ImmutableProgram,
    Processor,
)


@pytest.fixture
def processor() -> Processor:
    return Processor()


@pytest.fixture
def hardware(processor) -> Hardware:
    return Hardware(processor)


@pytest.fixture
def computer(hardware) -> Computer:
    return Computer(hardware)


@pytest.fixture
def empty_program() -> ImmutableProgram:
    return ImmutableProgram(instructions=[])


@pytest.fixture
def set_value_instruction():
    @dataclass(frozen=True)
    class _SetValueInstruction:
        register: Hashable
        value: int

        def execute(self, hardware: Hardware) -> None:
            hardware.processor.set_value_at_register(self.register, self.value)
            hardware.processor.increment_program_counter()

    def _instruction(register, value):
        return _SetValueInstruction(register, value)

    return _instruction


@pytest.fixture
def jump_instruction():
    @dataclass(frozen=True)
    class _JumpInstruction:
        increment: int

        def execute(self, hardware: Hardware) -> None:
            hardware.processor.increment_program_counter(self.increment)

    def _instruction(increment):
        return _JumpInstruction(increment)

    return _instruction


@pytest.fixture
def no_branch_program(set_value_instruction) -> ImmutableProgram:
    return ImmutableProgram(
        instructions=[
            set_value_instruction("a", 123),
            set_value_instruction("b", 321),
            set_value_instruction("c", 444),
        ]
    )


@pytest.fixture
def jump_program(set_value_instruction, jump_instruction) -> ImmutableProgram:
    return ImmutableProgram(
        instructions=[
            set_value_instruction("a", 123),
            set_value_instruction("b", 321),
            jump_instruction(increment=2),
            set_value_instruction("c", 444),
        ]
    )


def test_computer_running_empty_program_does_nothing(
    computer, processor, empty_program
):
    computer.run(empty_program)
    assert all(
        processor.get_value_at_register(register) == 0
        for register in ("a", "b", "c")
    )


def test_computer_runs_all_instructions_in_simple_program(
    computer, processor, no_branch_program
):
    computer.run(no_branch_program)
    assert processor.get_value_at_register("a") == 123
    assert processor.get_value_at_register("b") == 321
    assert processor.get_value_at_register("c") == 444


def test_computer_program_may_jump(computer, processor, jump_program):
    computer.run(jump_program)
    assert processor.get_value_at_register("a") == 123
    assert processor.get_value_at_register("b") == 321
    assert processor.get_value_at_register("c") == 0


def test_computer_can_run_one_instruction_at_a_time(
    computer, processor, no_branch_program
):
    computer.run_next_instruction(no_branch_program)
    assert processor.get_value_at_register("a") == 123
    assert processor.get_value_at_register("b") == 0
    computer.run_next_instruction(no_branch_program)
    assert processor.get_value_at_register("a") == 123
    assert processor.get_value_at_register("b") == 321
