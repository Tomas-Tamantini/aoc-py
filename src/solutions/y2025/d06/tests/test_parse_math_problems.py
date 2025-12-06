from src.solutions.y2025.d06.logic.math_homework import CephalopodMathProblem
from src.solutions.y2025.d06.logic.parser import (
    parse_math_problems_by_column,
    parse_math_problems_by_row,
)

CONTENT = (
    "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  \n"
)


def test_parse_math_problems_by_row(input_reader):
    reader = input_reader(CONTENT)
    problems = list(parse_math_problems_by_row(reader))
    assert problems == [
        CephalopodMathProblem(numbers=(123, 45, 6), operator="*"),
        CephalopodMathProblem(numbers=(328, 64, 98), operator="+"),
        CephalopodMathProblem(numbers=(51, 387, 215), operator="*"),
        CephalopodMathProblem(numbers=(64, 23, 314), operator="+"),
    ]


def test_parse_math_problems_by_column(input_reader):
    reader = input_reader(CONTENT)
    problems = list(parse_math_problems_by_column(reader))
    assert problems == [
        CephalopodMathProblem(numbers=(4, 431, 623), operator="+"),
        CephalopodMathProblem(numbers=(175, 581, 32), operator="*"),
        CephalopodMathProblem(numbers=(8, 248, 369), operator="+"),
        CephalopodMathProblem(numbers=(356, 24, 1), operator="*"),
    ]
