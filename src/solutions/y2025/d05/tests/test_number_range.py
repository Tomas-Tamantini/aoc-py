import pytest

from src.solutions.y2025.d05.logic.number_range import NumberRange


@pytest.mark.parametrize("n", [1, 3, 4])
def test_number_range_contains(n):
    assert NumberRange(1, 4).contains(n)


@pytest.mark.parametrize("n", [-1, 0, 5])
def test_number_range_does_not_contains(n):
    assert not NumberRange(1, 4).contains(n)
