from queue import Queue

from src.solutions.shared.vm import Computer, Hardware, Processor
from src.solutions.y2019.d23.logic.network_io import NodeInput, NodeOutput
from src.solutions.y2019.d23.logic.packet import Packet
from src.solutions.y2019.intcode import IntcodeProgram


class NetworkNode:
    def __init__(
        self,
        address: int,
        instructions: list[int],
        outgoing_packet_queue: Queue,
    ):
        self._program = IntcodeProgram(instructions)
        self._serial_input = NodeInput(address=address)
        self._computer = Computer(
            Hardware(
                processor=Processor(),
                memory=self._program,
                serial_input=self._serial_input,
                serial_output=NodeOutput(
                    address=address,
                    outgoing_packet_queue=outgoing_packet_queue,
                ),
            )
        )

    def is_idle(self) -> bool:
        return self._serial_input.is_idle

    def enqueue(self, packet: Packet) -> None:
        self._serial_input.enqueue(packet)

    def run_next_instruction(self) -> None:
        self._computer.run_next_instruction(self._program)

    def run_until_idle(self) -> None:
        while not self.is_idle():
            self.run_next_instruction()
