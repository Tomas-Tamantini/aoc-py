from queue import Queue

from src.solutions.y2019.d25.logic.droid_controller import DroidController


class DroidInput:
    def __init__(self, controller: DroidController):
        self._controller = controller
        self._buffer = Queue()

    def _get_next_command(self) -> None:
        cmd = self._controller.get_next_command()
        for c in cmd:
            self._buffer.put(ord(c))
        self._buffer.put(ord("\n"))

    def read_next(self) -> int:
        if self._buffer.empty():
            self._get_next_command()
        return self._buffer.get()
