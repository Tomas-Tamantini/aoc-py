from typing import Callable, Iterator

import pytest

from src.core.input_reader import InputReader


class _MockReader:
    def __init__(self, input_string: str):
        self._input_string = input_string

    def read_input(self) -> str:
        return self._input_string

    def read_lines(self) -> Iterator[str]:
        yield from self._input_string.splitlines()

    def read_stripped_lines(
        self, keep_empty_lines: bool = False
    ) -> Iterator[str]:
        for line in self._input_string.splitlines():
            stripped = line.strip()
            if stripped or keep_empty_lines:
                yield stripped


@pytest.fixture
def input_reader() -> Callable[[str], InputReader]:
    def _input_reader(input_string: str) -> InputReader:
        return _MockReader(input_string)

    return _input_reader
