import pytest

from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2015.d06.logic.light_grid import (
    DecreaseBrightnessInstruction,
    IncreaseBrightnessInstruction,
    ToggleInstruction,
    TurnOffInstruction,
    TurnOnInstruction,
)
from src.solutions.y2015.d06.logic.parse_light_grid_instructions import (
    parse_light_grid_instructions,
)


@pytest.fixture
def reader(input_reader):
    return input_reader(
        """
        turn on 0,0 through 999,999
        toggle 0,0 through 999,0
        turn off 499,499 through 500,500
        """
    )


def test_parse_light_grid_instructions(reader):
    instructions = list(parse_light_grid_instructions(reader))
    assert instructions == [
        TurnOnInstruction(BoundingBox([Vector2D(0, 0), Vector2D(999, 999)])),
        ToggleInstruction(BoundingBox([Vector2D(0, 0), Vector2D(999, 0)])),
        TurnOffInstruction(
            BoundingBox([Vector2D(499, 499), Vector2D(500, 500)])
        ),
    ]


def test_parse_light_grid_instructions_translated(reader):
    instructions = list(
        parse_light_grid_instructions(reader, translate_instructions=True)
    )
    assert instructions == [
        IncreaseBrightnessInstruction(
            BoundingBox([Vector2D(0, 0), Vector2D(999, 999)]),
            increase_amount=1,
        ),
        IncreaseBrightnessInstruction(
            BoundingBox([Vector2D(0, 0), Vector2D(999, 0)]), increase_amount=2
        ),
        DecreaseBrightnessInstruction(
            BoundingBox([Vector2D(499, 499), Vector2D(500, 500)])
        ),
    ]
