import pytest

from src.solutions.y2025.d10.logic.indicator_lights import (
    IndicatorLightsDiagram,
)
from src.solutions.y2025.d10.logic.optimize_presses import (
    min_presses_to_turn_lights_on,
)

DIAGRAMS = [
    IndicatorLightsDiagram(
        target_configuration=0b0110,
        buttons={0b0001, 0b0101, 0b0010, 0b0011, 0b1010, 0b1100},
    ),
    IndicatorLightsDiagram(
        target_configuration=0b00010,
        buttons={0b10111, 0b00110, 0b10001, 0b11100, 0b01111},
    ),
]


@pytest.mark.parametrize(
    ("diagram", "expected"), [(DIAGRAMS[0], 2), (DIAGRAMS[1], 3)]
)
def test_min_button_presses_to_turn_lights_on(diagram, expected):
    assert min_presses_to_turn_lights_on(diagram) == expected
