from queue import Queue


class AmplifierIO:
    class EmptyQueueError(Exception): ...

    def __init__(self) -> None:
        self._queue = Queue()
        self._last_output = -1

    def read_next(self) -> int:
        if self._queue.empty():
            raise AmplifierIO.EmptyQueueError()
        return self._queue.get()

    def put(self, value: int) -> None:
        self._queue.put(value)
        self._last_output = value

    @property
    def last_output(self) -> int:
        return self._last_output
