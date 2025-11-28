from queue import Queue
from typing import Optional

from src.solutions.y2019.d23.logic.network_node import NetworkNode
from src.solutions.y2019.d23.logic.packet import Packet


class NetworkMonitor:
    def __init__(self, address: int) -> None:
        self._address = address
        self._last_packet: Optional[Packet] = None

    @property
    def address(self) -> int:
        return self._address

    @staticmethod
    def network_is_idle(nodes: list[NetworkNode], packet_queue: Queue) -> bool:
        return packet_queue.empty() and all(n.is_idle() for n in nodes)

    def send(self, packet: Packet) -> None:
        self._last_packet = packet

    def kickstart_packet(self) -> Packet:
        if not self._last_packet:
            return Packet(self.address, destination=-1, x=0, y=0)
        else:
            return Packet(
                origin=self.address,
                destination=0,
                x=self._last_packet.x,
                y=self._last_packet.y,
            )
