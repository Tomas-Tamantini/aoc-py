from queue import Queue

from src.solutions.y2019.d23.logic.packet import Packet


class NodeInput:
    def __init__(self, address: int):
        self._values = Queue()
        self._values.put(address)
        self._num_misses = 0

    def read_next(self) -> int:
        if self._values.empty():
            self._num_misses += 1
            return -1
        else:
            self._num_misses = 0
            return self._values.get()

    def enqueue(self, packet: Packet) -> None:
        self._num_misses = 0
        self._values.put(packet.x)
        self._values.put(packet.y)

    @property
    def is_idle(self) -> bool:
        return self._num_misses >= 2


class NodeOutput:
    def __init__(self, address: int, outgoing_packet_queue: Queue) -> None:
        self._address = address
        self._outgoing_packet_queue = outgoing_packet_queue
        self._buffer = []

    def put(self, value: int) -> None:
        self._buffer.append(value)
        if len(self._buffer) == 3:
            self._outgoing_packet_queue.put(
                Packet(self._address, *self._buffer)
            )
            self._buffer.clear()
