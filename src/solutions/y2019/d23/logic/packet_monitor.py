from typing import Protocol

from src.solutions.y2019.d23.logic.packet import Packet


class PacketMonitor(Protocol):
    def record(self, packet: Packet) -> None: ...

    def stop_criteria_met(self) -> bool: ...
