from typing import Iterator, Protocol


class InputReader(Protocol):
    def read_input(self) -> str: ...

    def read_lines(self) -> Iterator[str]: ...

    def read_stripped_lines(
        self, keep_empty_lines: bool = False
    ) -> Iterator[str]: ...
