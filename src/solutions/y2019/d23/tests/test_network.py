import pytest

from src.solutions.y2019.d23.logic.network import run_network
from src.solutions.y2019.d23.logic.packet import Packet
from src.solutions.y2019.d23.logic.packet_monitor import PacketMonitor


@pytest.fixture
def instructions() -> list[int]:
    # A program in which:
    #   * Each computer receives a packet
    #   * They increment x, y by one and send it to the next computer
    #   * The first computer kickstarts with packet (x = 42, y = 13, dest = 1)
    #
    # Variable positions
    #   - network_address: 1000
    #   - destination_address: 1001
    #   - x: 2000
    #   - y: 2001
    #
    # Subroutine positions:
    #   - KickstartNetwork: 30
    #   - ReceivePacket: 9
    #   - SendPacket: 21

    return [
        3,
        1000,  # input network_address
        101,
        1,
        1000,
        1001,  # destination = network_address + 1
        1006,
        1000,
        30,  # if network_address == 0 GOTO KickstartNetwork
        # --------------------------
        # ------ ReceivePacket -----
        # --------------------------
        3,
        2000,  # input x
        3,
        2001,  # input y
        101,
        1,
        2000,
        2000,  # x += 1
        101,
        1,
        2001,
        2001,  # y += 1
        # --------------------------
        # ------- SendPacket -------
        # --------------------------
        4,
        1001,  # output destination
        4,
        2000,  # output x
        4,
        2001,  # output y
        1106,
        0,
        9,  # GOTO ReceivePacket
        # --------------------------
        # ---- KickstartNetwork ----
        # --------------------------
        1101,
        42,
        0,
        2000,  # x = 42
        1101,
        13,
        0,
        2001,  # y = 13
        1106,
        0,
        21,  # GOTO SendPacket
    ]


@pytest.fixture
def packet_monitor() -> PacketMonitor:
    class MockMonitor:
        def __init__(self):
            self.packet_history = []

        def record(self, packet: Packet) -> None:
            self.packet_history.append(packet)

        def stop_criteria_met(self) -> bool:
            return any(p.x == 43 for p in self.packet_history)

    return MockMonitor()


def test_network_runs_until_stop_criterion(instructions, packet_monitor):
    run_network(
        num_computers=2,
        instructions=instructions,
        packet_monitor=packet_monitor,
    )
    kickstart_packet = Packet(origin=0, destination=1, x=42, y=13)
    second_packet = Packet(origin=1, destination=2, x=43, y=14)
    assert packet_monitor.packet_history[0] == kickstart_packet
    assert second_packet in packet_monitor.packet_history
