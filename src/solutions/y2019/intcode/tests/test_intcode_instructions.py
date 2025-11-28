from collections import defaultdict
from typing import Optional

import pytest

from src.solutions.shared.vm import (
    Hardware,
    Processor,
    SerialInput,
    SerialOutput,
)
from src.solutions.y2019.intcode.instructions import (
    RELATIVE_BASE_REGISTER,
    IntcodeAdd,
    IntcodeEquals,
    IntcodeHalt,
    IntcodeInput,
    IntcodeJumpIfFalse,
    IntcodeJumpIfTrue,
    IntcodeLessThan,
    IntcodeMultiply,
    IntcodeOutput,
    IntcodeParameter,
    IntcodeRelativeBaseOffset,
    ParameterMode,
)
from src.solutions.y2019.intcode.serial_io import (
    SimpleSerialInput,
    SimpleSerialOutput,
)


class _Memory:
    def __init__(self) -> None:
        self._values = defaultdict(int)

    def read(self, address: int) -> int:
        return self._values[address]

    def write(self, address: int, value: int) -> None:
        self._values[address] = value


def _setup_hardware(
    initial_pc: int = 0,
    initial_memory_values: Optional[dict[int, int]] = None,
    serial_input: Optional[SerialInput] = None,
    serial_output: Optional[SerialOutput] = None,
    relative_base: int = 0,
) -> Hardware:
    processor = Processor(
        program_counter=initial_pc,
        register_values={RELATIVE_BASE_REGISTER: relative_base},
    )
    memory = _Memory()
    if initial_memory_values:
        for address, value in initial_memory_values.items():
            memory.write(address, value)
    return Hardware(
        processor=processor,
        memory=memory,
        serial_input=serial_input if serial_input else SimpleSerialInput([0]),
        serial_output=serial_output if serial_output else SimpleSerialOutput(),
    )


def test_intcode_parameter_in_immediate_mode_evaluates_to_itself():
    hardware = _setup_hardware(
        initial_memory_values={123: 456}, relative_base=100
    )
    param = IntcodeParameter(value=123, mode=ParameterMode.IMMEDIATE)
    assert param.evaluate(hardware) == 123
    with pytest.raises(ValueError, match="Cannot extract address"):
        param.address(hardware)


def test_intcode_parameter_in_position_mode_uses_absolute_address():
    hardware = _setup_hardware(
        initial_memory_values={123: 456}, relative_base=100
    )
    param = IntcodeParameter(value=123, mode=ParameterMode.POSITION)
    assert param.evaluate(hardware) == 456
    assert param.address(hardware) == 123


def test_intcode_parameter_in_relative_mode_uses_relative_address():
    hardware = _setup_hardware(
        initial_memory_values={223: 456}, relative_base=100
    )
    param = IntcodeParameter(value=123, mode=ParameterMode.RELATIVE)
    assert param.evaluate(hardware) == 456
    assert param.address(hardware) == 223


def test_intcode_halt_sets_pc_to_negative_one():
    hardware = _setup_hardware()
    instruction = IntcodeHalt()
    instruction.execute(hardware)
    assert hardware.processor.program_counter == -1


def _build_instruction(instruction_cls):
    num_params = {
        IntcodeHalt: 0,
        IntcodeAdd: 3,
        IntcodeMultiply: 3,
        IntcodeInput: 1,
        IntcodeOutput: 1,
        IntcodeLessThan: 3,
        IntcodeEquals: 3,
        IntcodeRelativeBaseOffset: 1,
    }[instruction_cls]
    params = (
        IntcodeParameter(i, ParameterMode.POSITION) for i in range(num_params)
    )
    return instruction_cls(*params)


@pytest.mark.parametrize(
    ("instruction", "increment"),
    [
        (_build_instruction(IntcodeAdd), 4),
        (_build_instruction(IntcodeMultiply), 4),
        (_build_instruction(IntcodeInput), 2),
        (_build_instruction(IntcodeOutput), 2),
        (_build_instruction(IntcodeLessThan), 4),
        (_build_instruction(IntcodeEquals), 4),
        (_build_instruction(IntcodeRelativeBaseOffset), 2),
    ],
)
def test_non_jump_intcode_instructions_increment_pc_by_proper_amount(
    instruction, increment
):
    initial_pc = 100
    hardware = _setup_hardware(initial_pc=initial_pc)
    instruction.execute(hardware)
    assert hardware.processor.program_counter == initial_pc + increment


@pytest.mark.parametrize(
    ("mode_first_param", "mode_second_param", "expected"),
    [
        (ParameterMode.POSITION, ParameterMode.POSITION, 444),
        (ParameterMode.POSITION, ParameterMode.IMMEDIATE, 125),
        (ParameterMode.IMMEDIATE, ParameterMode.POSITION, 322),
        (ParameterMode.IMMEDIATE, ParameterMode.IMMEDIATE, 3),
    ],
)
def test_intcode_add_stores_sum_of_inputs_with_given_modes(
    mode_first_param, mode_second_param, expected
):
    instruction = IntcodeAdd(
        input_a=IntcodeParameter(value=1, mode=mode_first_param),
        input_b=IntcodeParameter(value=2, mode=mode_second_param),
        output=IntcodeParameter(value=3, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_memory_values={1: 123, 2: 321})
    instruction.execute(hardware)
    assert hardware.memory.read(address=3) == expected


@pytest.mark.parametrize(
    ("mode_first_param", "mode_second_param", "expected"),
    [
        (ParameterMode.POSITION, ParameterMode.POSITION, 77),
        (ParameterMode.POSITION, ParameterMode.IMMEDIATE, 14),
        (ParameterMode.IMMEDIATE, ParameterMode.POSITION, 11),
        (ParameterMode.IMMEDIATE, ParameterMode.IMMEDIATE, 2),
    ],
)
def test_intcode_multiply_stores_product_of_inputs_with_given_modes(
    mode_first_param, mode_second_param, expected
):
    instruction = IntcodeMultiply(
        input_a=IntcodeParameter(value=1, mode=mode_first_param),
        input_b=IntcodeParameter(value=2, mode=mode_second_param),
        output=IntcodeParameter(value=3, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_memory_values={1: 7, 2: 11})
    instruction.execute(hardware)
    assert hardware.memory.read(address=3) == expected


def test_intcode_input_stores_input_at_given_position():
    instruction = IntcodeInput(
        store_at=IntcodeParameter(value=123, mode=ParameterMode.POSITION)
    )
    hardware = _setup_hardware(serial_input=SimpleSerialInput([42]))
    instruction.execute(hardware)
    assert hardware.memory.read(address=123) == 42


@pytest.mark.parametrize(
    ("mode", "expected"),
    [(ParameterMode.POSITION, 42), (ParameterMode.IMMEDIATE, 123)],
)
def test_intcode_output_outputs_param_value(mode, expected):
    serial_output = SimpleSerialOutput()
    instruction = IntcodeOutput(source=IntcodeParameter(value=123, mode=mode))
    hardware = _setup_hardware(
        initial_memory_values={123: 42}, serial_output=serial_output
    )
    instruction.execute(hardware)
    assert serial_output.last_output == expected


@pytest.mark.parametrize(
    "mode_first_param", [ParameterMode.IMMEDIATE, ParameterMode.POSITION]
)
def test_jump_if_true_does_not_jump_if_value_is_zero(mode_first_param):
    instruction = IntcodeJumpIfTrue(
        value=IntcodeParameter(value=0, mode=mode_first_param),
        jump_to=IntcodeParameter(value=321, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_pc=100, initial_memory_values={0: 0})
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 103


@pytest.mark.parametrize(
    ("mode_second_param", "expected"),
    [(ParameterMode.POSITION, 42), (ParameterMode.IMMEDIATE, 321)],
)
def test_jump_if_true_jumps_if_value_is_not_zero(mode_second_param, expected):
    instruction = IntcodeJumpIfTrue(
        value=IntcodeParameter(value=123, mode=ParameterMode.IMMEDIATE),
        jump_to=IntcodeParameter(value=321, mode=mode_second_param),
    )
    hardware = _setup_hardware(initial_pc=100, initial_memory_values={321: 42})
    instruction.execute(hardware)
    assert hardware.processor.program_counter == expected


@pytest.mark.parametrize(
    "mode_first_param", [ParameterMode.IMMEDIATE, ParameterMode.POSITION]
)
def test_jump_if_false_does_not_jump_if_value_is_not_zero(mode_first_param):
    instruction = IntcodeJumpIfFalse(
        value=IntcodeParameter(value=1, mode=mode_first_param),
        jump_to=IntcodeParameter(value=321, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_pc=100, initial_memory_values={1: 1})
    instruction.execute(hardware)
    assert hardware.processor.program_counter == 103


@pytest.mark.parametrize(
    ("mode_second_param", "expected"),
    [(ParameterMode.POSITION, 42), (ParameterMode.IMMEDIATE, 321)],
)
def test_jump_if_true_jumps_if_value_is_zero(mode_second_param, expected):
    instruction = IntcodeJumpIfFalse(
        value=IntcodeParameter(value=0, mode=ParameterMode.IMMEDIATE),
        jump_to=IntcodeParameter(value=321, mode=mode_second_param),
    )
    hardware = _setup_hardware(initial_pc=100, initial_memory_values={321: 42})
    instruction.execute(hardware)
    assert hardware.processor.program_counter == expected


@pytest.mark.parametrize(
    ("value_a", "value_b", "expected"),
    [
        (100, 100, 0),
        (101, 100, 0),
        (99, 100, 1),
    ],
)
def test_intcode_less_than_writes_a_leq_b(value_a, value_b, expected):
    instruction = IntcodeLessThan(
        input_a=IntcodeParameter(value=value_a, mode=ParameterMode.IMMEDIATE),
        input_b=IntcodeParameter(value=value_b, mode=ParameterMode.IMMEDIATE),
        output=IntcodeParameter(value=123, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_memory_values={123: 42})
    instruction.execute(hardware)
    assert hardware.memory.read(address=123) == expected


@pytest.mark.parametrize(
    ("value_a", "value_b", "expected"),
    [
        (100, 100, 1),
        (101, 100, 0),
        (99, 100, 0),
    ],
)
def test_intcode_equals_than_writes_a_eq_b(value_a, value_b, expected):
    instruction = IntcodeEquals(
        input_a=IntcodeParameter(value=value_a, mode=ParameterMode.IMMEDIATE),
        input_b=IntcodeParameter(value=value_b, mode=ParameterMode.IMMEDIATE),
        output=IntcodeParameter(value=123, mode=ParameterMode.POSITION),
    )
    hardware = _setup_hardware(initial_memory_values={123: 42})
    instruction.execute(hardware)
    assert hardware.memory.read(address=123) == expected


def test_intcode_relative_base_offset_increments_relative_base():
    instruction = IntcodeRelativeBaseOffset(
        offset=IntcodeParameter(value=-7, mode=ParameterMode.IMMEDIATE)
    )
    hardware = _setup_hardware(relative_base=100)
    instruction.execute(hardware)
    assert (
        hardware.processor.get_value_at_register(RELATIVE_BASE_REGISTER) == 93
    )
