from typing import Iterator

from src.core.input_reader import InputReader


def parse_calories(input_reader: InputReader) -> Iterator[tuple[int, ...]]:
    current_calories: list[int] = []
    for line in input_reader.read_stripped_lines(keep_empty_lines=True):
        if line:
            current_calories.append(int(line))
        elif current_calories:
            yield tuple(current_calories)
            current_calories = []
    if current_calories:
        yield tuple(current_calories)
