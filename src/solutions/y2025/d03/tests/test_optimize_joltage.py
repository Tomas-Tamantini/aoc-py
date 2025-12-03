import pytest

from src.solutions.y2025.d03.logic.optimize_joltage import optimize_joltage


@pytest.mark.parametrize(
    ("battery_bank", "num_digits", "expected_joltage"),
    [
        (987654321111111, 2, 98),
        (811111111111119, 2, 89),
        (234234234234278, 2, 78),
        (818181911112111, 2, 92),
        (987654321111111, 12, 987654321111),
        (811111111111119, 12, 811111111119),
        (234234234234278, 12, 434234234278),
        (818181911112111, 12, 888911112111),
    ],
)
def test_optimize_joltage(battery_bank, num_digits, expected_joltage):
    batteries = tuple(int(digit) for digit in str(battery_bank))
    joltage = optimize_joltage(batteries, num_digits=num_digits)
    assert expected_joltage == joltage
