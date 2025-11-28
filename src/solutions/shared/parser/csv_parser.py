from typing import Callable, Iterator, Optional, TypeVar

from src.core.input_reader import InputReader

T = TypeVar("T")


def parse_csv(
    input_reader: InputReader,
    separator: str = ",",
    mapper: Optional[Callable[[tuple[str, ...]], T]] = None,
) -> Iterator[T]:
    if mapper is None:

        def _default_mapper(x):
            return x

        mapper = _default_mapper
    for line in input_reader.read_stripped_lines():
        values = (value.strip() for value in line.split(separator))
        yield mapper(tuple(values))  # type: ignore
