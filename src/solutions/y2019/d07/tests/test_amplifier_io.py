import pytest

from src.solutions.y2019.d07.logic.amplifier_io import AmplifierIO


def test_amplifier_io_queues_input_and_sends_to_output():
    io = AmplifierIO()
    values = (123, 321, 444)
    for value in values:
        io.put(value)
    output = tuple(io.read_next() for _ in range(3))
    assert output == values


def test_amplifier_io_raises_error_when_empty_queue():
    io = AmplifierIO()
    with pytest.raises(AmplifierIO.EmptyQueueError):
        io.read_next()


def test_amplifier_io_stores_last_output():
    io = AmplifierIO()
    io = AmplifierIO()
    values = (123, 321, 444)
    for value in values:
        io.put(value)
    assert io.last_output == 444
