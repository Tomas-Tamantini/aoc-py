from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2015.d06.logic.light_grid import (
    DecreaseBrightnessInstruction,
    IncreaseBrightnessInstruction,
    LightGrid,
    ToggleInstruction,
    TurnOffInstruction,
    TurnOnInstruction,
)


def test_light_grid_starts_with_no_lights_on():
    grid = LightGrid(10, 10)
    assert grid.total_brightness() == 0


def test_turning_lights_on_sets_them_to_one():
    grid = LightGrid(10, 10)
    region = BoundingBox([Vector2D(0, 0), Vector2D(4, 3)])
    instruction = TurnOnInstruction(region)
    instruction.apply(grid)
    assert grid.total_brightness() == 20


def test_turning_lights_on_multiple_times_does_not_increase_brightness():
    grid = LightGrid(10, 10)
    instruction_1 = TurnOnInstruction(
        BoundingBox([Vector2D(0, 0), Vector2D(4, 3)])
    )
    instruction_2 = TurnOnInstruction(
        BoundingBox([Vector2D(2, 1), Vector2D(6, 5)])
    )
    instruction_1.apply(grid)
    instruction_2.apply(grid)
    assert grid.total_brightness() == 36


def test_turning_lights_off_sets_them_to_zero():
    grid = LightGrid(10, 10)
    instruction_1 = TurnOnInstruction(
        BoundingBox([Vector2D(0, 0), Vector2D(4, 3)])
    )
    instruction_2 = TurnOffInstruction(
        BoundingBox([Vector2D(2, 1), Vector2D(6, 5)])
    )
    instruction_1.apply(grid)
    instruction_2.apply(grid)
    assert grid.total_brightness() == 11


def test_toggling_lights_changes_zero_to_one_and_one_to_zero():
    grid = LightGrid(10, 10)
    instruction_1 = TurnOnInstruction(
        BoundingBox([Vector2D(0, 0), Vector2D(4, 3)])
    )
    instruction_2 = ToggleInstruction(
        BoundingBox([Vector2D(2, 1), Vector2D(5, 6)])
    )
    instruction_1.apply(grid)
    instruction_2.apply(grid)
    assert grid.total_brightness() == 26


def test_increasing_brightness_increases_by_given_amount():
    grid = LightGrid(10, 10)
    instruction_1 = IncreaseBrightnessInstruction(
        BoundingBox([Vector2D(0, 0), Vector2D(4, 3)]), increase_amount=2
    )
    instruction_2 = IncreaseBrightnessInstruction(
        BoundingBox([Vector2D(2, 1), Vector2D(5, 6)]), increase_amount=3
    )
    instruction_1.apply(grid)
    instruction_2.apply(grid)
    assert grid.total_brightness() == 112


def test_decreasing_brightness_decreases_by_one_to_minimum_of_zero():
    grid = LightGrid(10, 10)
    instruction_1 = IncreaseBrightnessInstruction(
        BoundingBox([Vector2D(0, 0), Vector2D(4, 3)]), increase_amount=2
    )
    instruction_2 = DecreaseBrightnessInstruction(
        BoundingBox([Vector2D(2, 1), Vector2D(5, 6)])
    )
    instruction_1.apply(grid)
    instruction_2.apply(grid)
    assert grid.total_brightness() == 31
