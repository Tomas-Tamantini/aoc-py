import pytest

from src.solutions.shared.number_theory.interval import Interval


@pytest.mark.parametrize("n", [1, 3, 4])
def test_interval_contains_number_if_within_range(n):
    assert Interval(1, 4).contains(n)


@pytest.mark.parametrize("n", [-1, 0, 5])
def test_interval_does_not_contain_number_if_outside_range(n):
    assert not Interval(1, 4).contains(n)


def test_intervals_are_sorted_by_range_start():
    int_a = Interval(10, 20)
    int_b = Interval(3, 30)
    int_c = Interval(7, 8)

    sorted_intervals = sorted([int_a, int_b, int_c])
    assert sorted_intervals == [int_b, int_c, int_a]


def test_intervals_intersect_if_some_number_in_common():
    assert Interval(10, 20).intersects(Interval(20, 30))
    assert Interval(10, 20).intersects(Interval(5, 10))
    assert Interval(10, 20).intersects(Interval(9, 21))
    assert not Interval(10, 20).intersects(Interval(21, 30))
