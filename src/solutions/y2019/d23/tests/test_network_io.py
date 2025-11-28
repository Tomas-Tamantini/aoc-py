from queue import Queue

import pytest

from src.solutions.y2019.d23.logic.network_io import NodeInput, NodeOutput
from src.solutions.y2019.d23.logic.packet import Packet


@pytest.fixture
def node_input() -> NodeInput:
    return NodeInput(address=123)


def _packet(x: int = 1, y: int = 2) -> Packet:
    return Packet(origin=321, destination=123, x=x, y=y)


def test_node_input_yields_address_first():
    node_input = NodeInput(address=123)
    assert node_input.read_next() == 123


def test_node_input_allows_enqueing_packages(node_input):
    node_input.enqueue(_packet(x=10, y=20))
    node_input.enqueue(_packet(x=30, y=40))
    values = [node_input.read_next() for _ in range(5)]
    assert values == [123, 10, 20, 30, 40]


def test_node_input_returns_negative_one_if_empty_queue(node_input):
    node_input.read_next()
    assert node_input.read_next() == -1


def test_node_input_starts_not_idle(node_input):
    assert not node_input.is_idle


def test_node_input_is_idle_if_two_or_more_empty_reads_and_empty_queue(
    node_input,
):
    node_input.read_next()
    assert not node_input.is_idle
    node_input.read_next()
    assert not node_input.is_idle
    node_input.read_next()
    assert node_input.is_idle
    node_input.enqueue(_packet())
    assert not node_input.is_idle


def test_node_output_builds_packet_from_address_x_and_y():
    queue = Queue()
    node_output = NodeOutput(address=123, outgoing_packet_queue=queue)
    for value in (456, 10, 20, 789, 30, 40):
        node_output.put(value)
    assert queue.get() == Packet(origin=123, destination=456, x=10, y=20)
    assert queue.get() == Packet(origin=123, destination=789, x=30, y=40)
