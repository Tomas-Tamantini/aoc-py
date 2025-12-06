from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2025.d06.logic.math_homework import CephalopodMathProblem


def parse_math_problems_by_row(
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


def _read_columns_left_to_right(input_reader: InputReader) -> Iterator[str]:
    lines = list(input_reader.read_lines())
    height = len(lines)
    width = len(lines[0])
    for col in reversed(range(width)):
        col_str = "".join(lines[row][col] for row in range(height)).strip()
        if col_str:
            yield col_str


def parse_math_problems_by_column(
    input_reader: InputReader,
) -> Iterator[CephalopodMathProblem]:
    numbers = []
    for col in _read_columns_left_to_right(input_reader):
        if col[-1] in "+*":
            numbers.append(int(col[:-1]))
            yield CephalopodMathProblem(
                numbers=tuple(numbers), operator=col[-1]
            )
            numbers = []
        else:
            numbers.append(int(col))
