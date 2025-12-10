import pytest

from src.solutions.y2025.d10.logic.machine import Machine
from src.solutions.y2025.d10.logic.optimize_indicator_lights import (
    min_presses_to_turn_lights_on,
)
from src.solutions.y2025.d10.logic.optimize_joltage import (
    min_presses_to_reach_joltage,
)

MACHINES = [
    Machine(
        target_indicator_lights=(False, True, True, False),
        button_wirings=((3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)),
        target_joltage=(3, 5, 4, 7),
    ),
    Machine(
        target_indicator_lights=(False, False, False, True, False),
        button_wirings=(
            (0, 2, 3, 4),
            (2, 3),
            (0, 4),
            (0, 1, 2),
            (1, 2, 3, 4),
        ),
        target_joltage=(7, 5, 12, 7, 2),
    ),
]


@pytest.mark.parametrize(
    ("machine", "expected"), [(MACHINES[0], 2), (MACHINES[1], 3)]
)
def test_min_button_presses_to_turn_lights_on(machine, expected):
    assert min_presses_to_turn_lights_on(machine) == expected


@pytest.mark.parametrize(
    ("machine", "expected"), [(MACHINES[0], 10), (MACHINES[1], 12)]
)
def test_min_button_presses_to_reach_target_joltage(machine, expected):
    assert min_presses_to_reach_joltage(machine) == expected
