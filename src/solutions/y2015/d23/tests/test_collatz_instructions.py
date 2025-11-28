import pytest

from src.solutions.shared.vm import Hardware, Processor
from src.solutions.y2015.d23.logic.collatz_instructions import (
    CollatzHalveInstruction,
    CollatzIncrementInstruction,
    CollatzJumpIfEvenInstruction,
    CollatzJumpIfOneInstruction,
    CollatzJumpInstruction,
    CollatzTripleInstruction,
)


@pytest.fixture
def processor():
    return Processor(
        register_values={"a": 123, "b": 124, "c": 1}, program_counter=10
    )


def test_collatz_halve_instruction_halves_register_and_increments_pc_by_one(
    processor,
):
    instruction = CollatzHalveInstruction(register="a")
    instruction.execute(Hardware(processor))
    assert processor.get_value_at_register("a") == 61
    assert processor.program_counter == 11


def test_collatz_triple_instruction_triples_register_and_increments_pc_by_one(
    processor,
):
    instruction = CollatzTripleInstruction(register="a")
    instruction.execute(Hardware(processor))
    assert processor.get_value_at_register("a") == 369
    assert processor.program_counter == 11


def test_collatz_increment_instruction_incs_register_and_increments_pc_by_one(
    processor,
):
    instruction = CollatzIncrementInstruction(register="a")
    instruction.execute(Hardware(processor))
    assert processor.get_value_at_register("a") == 124
    assert processor.program_counter == 11


def test_collatz_jump_instruction_increments_program_counter_by_offset(
    processor,
):
    instruction = CollatzJumpInstruction(offset=-3)
    instruction.execute(Hardware(processor))
    assert processor.program_counter == 7


def test_collatz_jump_if_even_increments_program_counter_by_one_if_odd(
    processor,
):
    instruction = CollatzJumpIfEvenInstruction(register="a", offset=3)
    instruction.execute(Hardware(processor))
    assert processor.program_counter == 11


def test_collatz_jump_if_even_increments_program_counter_by_offset_if_even(
    processor,
):
    instruction = CollatzJumpIfEvenInstruction(register="b", offset=3)
    instruction.execute(Hardware(processor))
    assert processor.program_counter == 13


def test_collatz_jump_if_one_increments_program_counter_by_one_if_not_one(
    processor,
):
    instruction = CollatzJumpIfOneInstruction(register="a", offset=3)
    instruction.execute(Hardware(processor))
    assert processor.program_counter == 11


def test_collatz_jump_if_one_increments_program_counter_by_offset_if_one(
    processor,
):
    instruction = CollatzJumpIfOneInstruction(register="c", offset=3)
    instruction.execute(Hardware(processor))
    assert processor.program_counter == 13
