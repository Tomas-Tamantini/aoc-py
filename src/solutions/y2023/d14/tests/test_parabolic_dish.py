from typing import Optional

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2023.d14.logic.parabolic_dish import ParabolicDish


def _dish(
    width: int = 6,
    height: int = 5,
    cube_rock_positions: Optional[set[Vector2D]] = None,
    rounded_rock_positions: Optional[set[Vector2D]] = None,
) -> ParabolicDish:
    cube_rock_positions = cube_rock_positions or set()
    rounded_rock_positions = rounded_rock_positions or set()
    return ParabolicDish(
        width=width,
        height=height,
        cube_rock_positions=cube_rock_positions,
        rounded_rock_positions=rounded_rock_positions,
    )


def test_rounded_rock_does_not_leave_dish():
    dish = _dish(rounded_rock_positions={Vector2D(0, 0)})
    assert dish.rounded_rock_positions == {Vector2D(0, 0)}
    dish = dish.tilt(Direction.UP)
    assert dish.rounded_rock_positions == {Vector2D(0, 4)}
    dish = dish.tilt(Direction.RIGHT)
    assert dish.rounded_rock_positions == {Vector2D(5, 4)}
    dish = dish.tilt(Direction.DOWN)
    assert dish.rounded_rock_positions == {Vector2D(5, 0)}
    dish = dish.tilt(Direction.LEFT)
    assert dish.rounded_rock_positions == {Vector2D(0, 0)}


def test_rounded_rock_does_not_roll_over_other_rounded_rock():
    dish = _dish(
        rounded_rock_positions={
            Vector2D(0, 0),
            Vector2D(1, 0),
            Vector2D(0, 1),
        }
    )
    dish = dish.tilt(Direction.UP)
    assert dish.rounded_rock_positions == {
        Vector2D(0, 3),
        Vector2D(1, 4),
        Vector2D(0, 4),
    }
    dish = dish.tilt(Direction.RIGHT)
    assert dish.rounded_rock_positions == {
        Vector2D(5, 3),
        Vector2D(4, 4),
        Vector2D(5, 4),
    }
    dish = dish.tilt(Direction.DOWN)
    assert dish.rounded_rock_positions == {
        Vector2D(5, 0),
        Vector2D(4, 0),
        Vector2D(5, 1),
    }
    dish = dish.tilt(Direction.LEFT)
    assert dish.rounded_rock_positions == {
        Vector2D(0, 0),
        Vector2D(1, 0),
        Vector2D(0, 1),
    }


def test_rounded_rock_does_not_roll_over_cube_rocks():
    dish = _dish(
        rounded_rock_positions={Vector2D(0, 0)},
        cube_rock_positions={
            Vector2D(0, 4),
            Vector2D(5, 3),
            Vector2D(4, 0),
            Vector2D(1, 1),
        },
    )
    dish = dish.tilt(Direction.UP)
    assert dish.rounded_rock_positions == {Vector2D(0, 3)}
    dish = dish.tilt(Direction.RIGHT)
    assert dish.rounded_rock_positions == {Vector2D(4, 3)}
    dish = dish.tilt(Direction.DOWN)
    assert dish.rounded_rock_positions == {Vector2D(4, 1)}
    dish = dish.tilt(Direction.LEFT)
    assert dish.rounded_rock_positions == {Vector2D(2, 1)}
