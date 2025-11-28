from typing import Optional

from src.core.io_handler import IOHandler
from src.solutions.y2019.d23.logic.network import run_network
from src.solutions.y2019.d23.logic.packet import Packet
from src.solutions.y2019.intcode import parse_instructions


class _PacketMonitor:
    def __init__(self):
        self._first_sent_to_nat: Optional[Packet] = None
        self._first_duplicate_y: Optional[int] = None
        self._last_y: Optional[int] = None

    @property
    def first_sent_to_nat(self) -> Packet:
        if not self._first_sent_to_nat:
            raise ValueError("No packet has been sent to NAT")
        else:
            return self._first_sent_to_nat

    @property
    def first_duplicate_y(self) -> int:
        if self._first_duplicate_y is None:
            raise ValueError("No duplicate y values")
        else:
            return self._first_duplicate_y

    def record(self, packet: Packet) -> None:
        if packet.destination == 255 and not self._first_sent_to_nat:
            self._first_sent_to_nat = packet
        elif packet.origin == 255:
            if packet.y == self._last_y:
                self._first_duplicate_y = packet.y
            else:
                self._last_y = packet.y

    def stop_criteria_met(self) -> bool:
        return self._first_duplicate_y is not None


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 23

    instructions = parse_instructions(
        input_reader=io_handler.input_reader(*prob_id)
    )

    monitor = _PacketMonitor()

    run_network(
        num_computers=50, instructions=instructions, packet_monitor=monitor
    )

    io_handler.write_result(
        *prob_id, part=1, result=monitor.first_sent_to_nat.y
    )
    io_handler.write_result(*prob_id, part=2, result=monitor.first_duplicate_y)
