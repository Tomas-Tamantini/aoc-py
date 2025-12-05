import pytest

from src.solutions.shared.number_theory.interval import Interval


def test_interval_size_is_member_count():
    assert Interval(101, 900).size == 800


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


@pytest.mark.parametrize(
    ("interval_a", "interval_b", "intersection"),
    [
        (Interval(10, 20), Interval(30, 40), None),
        (Interval(10, 20), Interval(15, 30), Interval(10, 30)),
        (Interval(10, 20), Interval(10, 12), Interval(10, 20)),
        (Interval(10, 20), Interval(5, 9), Interval(5, 20)),
    ],
)
def test_interval_union_yields_new_interval_if_possible(
    interval_a, interval_b, intersection
):
    assert interval_a.union(interval_b) == intersection
