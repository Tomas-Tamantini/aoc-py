import pytest

from src.solutions.shared.number_theory.interval import Interval
from src.solutions.y2025.d05.logic.interval_union import union_size


@pytest.mark.parametrize(
    ("intervals", "expected"),
    [
        ([], 0),
        ([Interval(1, 1_000_000)], 1_000_000),
        ([Interval(1, 5), Interval(11, 13)], 8),
        (
            [
                Interval(12, 20),
                Interval(3, 4),
                Interval(11, 13),
                Interval(1, 5),
            ],
            15,
        ),
    ],
)
def test_intervals_union_have_proper_size(intervals, expected):
    assert union_size(intervals) == expected
