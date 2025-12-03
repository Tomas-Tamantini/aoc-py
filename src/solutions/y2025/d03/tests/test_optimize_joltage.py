import pytest

from src.solutions.y2025.d03.logic.optimize_joltage import optimize_joltage


@pytest.mark.parametrize(
    ("battery_bank", "expected_joltage"),
    [
        (987654321111111, 98),
        (811111111111119, 89),
        (234234234234278, 78),
        (818181911112111, 92),
    ],
)
def test_optimize_joltage(battery_bank, expected_joltage):
    batteries = tuple(int(digit) for digit in str(battery_bank))
    joltage = optimize_joltage(batteries)
    assert expected_joltage == joltage
