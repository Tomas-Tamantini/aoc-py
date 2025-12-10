import pytest

from src.solutions.y2025.d10.logic.indicator_lights import min_button_presses


@pytest.mark.parametrize(
    ("target_config", "buttons", "expected"),
    [
        (0b0110, {0b0001, 0b0101, 0b0010, 0b0011, 0b1010, 0b1100}, 2),
        (0b00010, {0b10111, 0b00110, 0b10001, 0b11100, 0b01111}, 3),
    ],
)
def test_min_button_presses_to_reach_indicator_lights(
    target_config, buttons, expected
):
    assert min_button_presses(target_config, buttons) == expected
