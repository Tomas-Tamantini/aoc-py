from src.solutions.y2025.d06.logic.math_homework import CephalopodMathProblem
from src.solutions.y2025.d06.logic.parser import parse_math_problems


def test_parse_math_problems(input_reader):
    reader = input_reader(
        "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  \n"
    )
    problems = list(parse_math_problems(reader))
    assert problems == [
        CephalopodMathProblem(numbers=(123, 45, 6), operator="*"),
        CephalopodMathProblem(numbers=(328, 64, 98), operator="+"),
        CephalopodMathProblem(numbers=(51, 387, 215), operator="*"),
        CephalopodMathProblem(numbers=(64, 23, 314), operator="+"),
    ]
