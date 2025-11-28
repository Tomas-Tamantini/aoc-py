from typing import Hashable

import pytest

from src.solutions.shared.vm import Hardware, Processor
from src.solutions.y2016.assembunny.instructions import (
    CopyInstruction,
    DecrementInstruction,
    IncrementInstruction,
    JumpNotZeroInstruction,
    LiteralValue,
    NoOpInstruction,
    RegisterValue,
)


@pytest.fixture
def set_hardware():
    def _set_hardware(register_a_value: int = 0):
        initial_registers: dict[Hashable, int] = {"a": register_a_value}
        processor = Processor(
            register_values=initial_registers, program_counter=1000
        )
        return Hardware(processor)

    return _set_hardware


def test_increment_instruction_increments_register_value_by_one_as_default(
    set_hardware,
):
    hardware = set_hardware(register_a_value=123)
    instruction = IncrementInstruction(register="a")
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("a") == 124


def test_increment_instruction_may_have_literal_increment(set_hardware):
    hardware = set_hardware(register_a_value=123)
    instruction = IncrementInstruction(register="a", value=LiteralValue(123))
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("a") == 246


def test_increment_instruction_may_have_register_increment(set_hardware):
    hardware = set_hardware(register_a_value=123)
    instruction = IncrementInstruction(register="b", value=RegisterValue("a"))
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("b") == 123


def test_decrement_instruction_decrements_register_value_by_one(set_hardware):
    hardware = set_hardware(register_a_value=123)
    instruction = DecrementInstruction(register="a")
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("a") == 122


def test_copy_instruction_copies_literal_value_into_register(set_hardware):
    hardware = set_hardware(register_a_value=123)
    instruction = CopyInstruction(register="a", value=LiteralValue(321))
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("a") == 321


def test_copy_instruction_copies_register_into_other_register(set_hardware):
    hardware = set_hardware(register_a_value=123)
    instruction = CopyInstruction(register="b", value=RegisterValue("a"))
    instruction.execute(hardware)
    assert hardware.processor.get_value_at_register("b") == 123


@pytest.mark.parametrize(
    "instruction",
    [
        IncrementInstruction(register="a"),
        DecrementInstruction(register="a"),
        CopyInstruction(register="a", value=LiteralValue(7)),
        NoOpInstruction(),
    ],
)
def test_non_jump_instructions_increment_pc_by_one(set_hardware, instruction):
    hardware = set_hardware()
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 1001


def test_jump_not_zero_instruction_does_not_jump_if_literal_value_is_zero(
    set_hardware,
):
    hardware = set_hardware()
    instruction = JumpNotZeroInstruction(value=LiteralValue(0), offset=3)
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 1001


def test_jump_not_zero_instruction_does_not_jump_if_register_value_is_zero(
    set_hardware,
):
    hardware = set_hardware(register_a_value=0)
    instruction = JumpNotZeroInstruction(value=RegisterValue("a"), offset=3)
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 1001


def test_jump_not_zero_instruction_jumps_if_literal_value_is_not_zero(
    set_hardware,
):
    hardware = set_hardware()
    instruction = JumpNotZeroInstruction(value=LiteralValue(17), offset=3)
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 1003


def test_jump_not_zero_instruction_jumps_if_register_value_is_not_zero(
    set_hardware,
):
    hardware = set_hardware(register_a_value=7)
    instruction = JumpNotZeroInstruction(value=RegisterValue("a"), offset=3)
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 1003
