import pytest

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2023.d14.logic.parabolic_dish import ParabolicDish
from src.solutions.y2023.d14.logic.run_cycle import run_cycle


@pytest.fixture
def dish():
    return ParabolicDish(
        width=6,
        height=5,
        rounded_rock_positions={Vector2D(0, 0)},
        cube_rock_positions={
            Vector2D(0, 4),
            Vector2D(5, 3),
            Vector2D(4, 0),
            Vector2D(1, 1),
        },
    )


def test_dish_cycles_are_run_correctly(dish):
    cycle = (Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT)
    dish = run_cycle(dish, cycle, num_cycles=2)
    assert dish.rounded_rock_positions == {Vector2D(1, 4)}


def test_dish_cycles_run_efficiently(dish):
    cycle = (Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT)
    dish = run_cycle(dish, cycle, num_cycles=2_000_000_000)
    assert dish.rounded_rock_positions == {Vector2D(1, 4)}
