import pytest

from src.solutions.shared.number_theory.interval import Interval


@pytest.mark.parametrize("n", [1, 3, 4])
def test_interval_contains_number_if_within_range(n):
    assert Interval(1, 4).contains(n)


@pytest.mark.parametrize("n", [-1, 0, 5])
def test_interval_does_not_contain_number_if_outside_range(n):
    assert not Interval(1, 4).contains(n)
