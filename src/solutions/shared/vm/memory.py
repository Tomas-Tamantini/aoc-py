from typing import Protocol


class Memory(Protocol):
    def read(self, address: int) -> int: ...

    def write(self, address: int, value: int) -> None: ...
