from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d06.logic.math_homework import CephalopodMathProblem


def parse_math_problems(
    input_reader: InputReader,
) -> Iterator[CephalopodMathProblem]:
    rows = []
    for row in input_reader.read_stripped_lines():
        values = tuple(value.strip() for value in row.split())
        rows.append(values)

    for operation_elements in zip(*rows):
        yield CephalopodMathProblem(
            numbers=tuple(map(int, operation_elements[:-1])),
            operator=operation_elements[-1],
        )
