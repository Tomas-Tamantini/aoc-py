import pytest

from src.solutions.y2025.d06.logic.math_homework import CephalopodMathProblem


@pytest.mark.parametrize(
    ("numbers", "operator", "expected"),
    [((123, 45, 6), "*", 33210), ((328, 64, 98), "+", 490)],
)
def test_cephalopod_math_problem_applies_operator_to_all_numbers(
    numbers, operator, expected
):
    problem = CephalopodMathProblem(numbers, operator)
    assert problem.evaluate() == expected
