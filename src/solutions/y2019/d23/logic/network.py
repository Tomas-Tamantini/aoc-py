from queue import Queue
from typing import Optional

from src.solutions.y2019.d23.logic.network_monitor import NetworkMonitor
from src.solutions.y2019.d23.logic.network_node import NetworkNode
from src.solutions.y2019.d23.logic.packet_monitor import PacketMonitor


def _non_idle_node(nodes: list[NetworkNode]) -> Optional[NetworkNode]:
    for node in nodes:
        if not node.is_idle():
            return node


def _build_nodes(
    num_computers: int, instructions: list[int], outgoing_packet_queue: Queue
) -> list[NetworkNode]:
    return [
        NetworkNode(
            address=i,
            instructions=instructions,
            outgoing_packet_queue=outgoing_packet_queue,
        )
        for i in range(num_computers)
    ]


def run_network(
    num_computers: int, instructions: list[int], packet_monitor: PacketMonitor
) -> None:
    packet_queue = Queue()
    nodes = _build_nodes(num_computers, instructions, packet_queue)
    monitor = NetworkMonitor(address=255)

    while not packet_monitor.stop_criteria_met():
        if node := _non_idle_node(nodes):
            node.run_until_idle()
        if not packet_queue.empty():
            packet = packet_queue.get()
            packet_monitor.record(packet)
            if packet.destination == monitor.address:
                monitor.send(packet)
            elif 0 <= packet.destination < num_computers:
                nodes[packet.destination].enqueue(packet)
        if monitor.network_is_idle(nodes, packet_queue):
            packet_queue.put(monitor.kickstart_packet())
