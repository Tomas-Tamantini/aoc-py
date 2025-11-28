from dataclasses import dataclass
from queue import Queue

import pytest

from src.solutions.y2019.d23.logic.network_monitor import NetworkMonitor
from src.solutions.y2019.d23.logic.packet import Packet


@dataclass
class _MockNode:
    idle: bool

    def is_idle(self) -> bool:
        return self.idle


@pytest.fixture
def monitor() -> NetworkMonitor:
    return NetworkMonitor(address=255)


def test_network_is_not_idle_if_some_packet_in_queue(monitor):
    queue = Queue()
    queue.put(Packet(origin=1, destination=2, x=3, y=4))
    nodes = []
    assert not monitor.network_is_idle(nodes, queue)


def test_network_is_not_idle_if_some_node_is_not_idle(monitor):
    queue = Queue()
    nodes = [_MockNode(idle=True), _MockNode(idle=False)]
    assert not monitor.network_is_idle(nodes, queue)


def test_network_is_idle_if_all_nodes_are_idle_and_queue_is_empty(monitor):
    queue = Queue()
    nodes = [_MockNode(idle=True), _MockNode(idle=True)]
    assert monitor.network_is_idle(nodes, queue)


def test_monitor_keeps_track_of_last_packet_and_sends_to_first_node(monitor):
    monitor.send(Packet(origin=123, destination=321, x=10, y=20))
    monitor.send(Packet(origin=456, destination=654, x=30, y=40))
    assert monitor.kickstart_packet() == Packet(
        origin=255, destination=0, x=30, y=40
    )
