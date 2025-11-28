import pytest

from src.solutions.y2019.d07.logic.amplifier import Amplifier
from src.solutions.y2019.d07.logic.amplifier_io import AmplifierIO
from src.solutions.y2019.intcode import IntcodeProgram


@pytest.fixture
def read_input_twice_program():
    # Transfer input to output twice and halt
    instructions = [3, 100, 4, 100, 3, 100, 4, 100, 99]
    return IntcodeProgram(instructions)


def test_amplifier_runs_until_empty_input_queue(read_input_twice_program):
    input_queue = AmplifierIO()
    output_queue = AmplifierIO()
    amplifier = Amplifier(
        program=read_input_twice_program,
        input_queue=input_queue,
        output_queue=output_queue,
    )
    input_queue.put(10)
    amplifier.resume_execution()
    assert output_queue.last_output == 10
    assert not amplifier.halted


def test_amplifier_runs_until_halted(read_input_twice_program):
    input_queue = AmplifierIO()
    output_queue = AmplifierIO()
    amplifier = Amplifier(
        program=read_input_twice_program,
        input_queue=input_queue,
        output_queue=output_queue,
    )
    input_queue.put(10)
    input_queue.put(20)
    input_queue.put(30)  # Should ignore, halted already
    amplifier.resume_execution()
    assert output_queue.last_output == 20
    assert amplifier.halted
