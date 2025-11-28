from typing import Protocol


class SerialInput(Protocol):
    def read_next(self) -> int: ...


class SerialOutput(Protocol):
    def put(self, value: int) -> None: ...
