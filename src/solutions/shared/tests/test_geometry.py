import pytest

from src.solutions.shared.geometry import (
    BoundingBox,
    Direction,
    HexagonalCoordinates,
    HexagonalDirection,
    Turn,
    Vector2D,
)


def test_vectors_can_be_sorted_lexicographically():
    v1 = Vector2D(1, 3)
    v2 = Vector2D(2, 1)
    v3 = Vector2D(1, 2)

    assert v3 < v1
    assert v1 < v2


def test_vectors_can_be_subtracted():
    v1 = Vector2D(5, 7)
    v2 = Vector2D(3, 4)
    diff = v1 - v2
    assert diff == Vector2D(2, 3)


def test_vectors_can_be_added():
    v1 = Vector2D(5, 7)
    v2 = Vector2D(3, 4)
    sum_vector = v1 + v2
    assert sum_vector == Vector2D(8, 11)


def test_vector_supports_integer_division():
    v = Vector2D(10, 15)
    assert v // 3 == Vector2D(3, 5)


def test_vectors_have_manhattan_size():
    assert Vector2D(2, -3).manhattan_size() == 5


def test_vectors_have_manhattan_distance():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(4, -2)
    assert v1.manhattan_distance(v2) == 7


def test_vector_neighbors_can_be_iterated():
    v = Vector2D(3, 4)
    neighbors = set(v.neighbors())
    assert neighbors == {
        Vector2D(4, 4),
        Vector2D(2, 4),
        Vector2D(3, 5),
        Vector2D(3, 3),
    }


def test_vector_neighbors_can_include_diagonals():
    v = Vector2D(3, 4)
    neighbors = set(v.neighbors(include_diagonals=True))
    assert neighbors == {
        Vector2D(4, 4),
        Vector2D(2, 4),
        Vector2D(3, 5),
        Vector2D(3, 3),
        Vector2D(4, 5),
        Vector2D(4, 3),
        Vector2D(2, 5),
        Vector2D(2, 3),
    }


def test_vector_can_move_in_given_direction():
    v = Vector2D(3, 4)
    assert v.move(Direction.UP) == Vector2D(3, 5)
    assert v.move(Direction.DOWN) == Vector2D(3, 3)
    assert v.move(Direction.LEFT) == Vector2D(2, 4)
    assert v.move(Direction.RIGHT) == Vector2D(4, 4)


def test_vector_can_move_any_number_of_steps():
    v = Vector2D(3, 4)
    assert v.move(Direction.UP, num_steps=5) == Vector2D(3, 9)


@pytest.mark.parametrize(
    ("direction", "turn", "expected"),
    [
        (Direction.RIGHT, Turn.LEFT, Direction.UP),
        (Direction.DOWN, Turn.RIGHT, Direction.LEFT),
        (Direction.LEFT, Turn.U_TURN, Direction.RIGHT),
        (Direction.UP, Turn.NO_TURN, Direction.UP),
    ],
)
def test_direction_can_be_turned(direction, turn, expected):
    assert direction.turn(turn) == expected


def test_direction_can_be_checked_for_horizontality():
    assert Direction.LEFT.is_horizontal
    assert Direction.RIGHT.is_horizontal
    assert not Direction.UP.is_horizontal
    assert not Direction.DOWN.is_horizontal


def test_vector_aligned_with_axes_can_be_normalized():
    assert Vector2D(0, -10).normalized() == Vector2D(0, -1)
    assert Vector2D(15, 0).normalized() == Vector2D(1, 0)


def test_vector_not_aligned_with_axes_cannot_be_normalized():
    with pytest.raises(ValueError, match="diagonal vector"):
        Vector2D(3, 4).normalized()


def test_zero_vector_cannot_be_normalized():
    with pytest.raises(ValueError, match="zero vector"):
        Vector2D(0, 0).normalized()


def test_bounding_box_keeps_track_of_min_and_max_coordinates():
    b = BoundingBox(
        points={Vector2D(10, 20), Vector2D(30, 18), Vector2D(9, 7)}
    )
    assert b.min_y == 7
    assert b.max_y == 20
    assert b.min_x == 9
    assert b.max_x == 30


@pytest.mark.parametrize(
    ("direction", "expected"),
    [
        (HexagonalDirection.EAST, HexagonalCoordinates(11, 20)),
        (HexagonalDirection.NORTHEAST, HexagonalCoordinates(10, 21)),
        (HexagonalDirection.NORTHWEST, HexagonalCoordinates(9, 21)),
        (HexagonalDirection.WEST, HexagonalCoordinates(9, 20)),
        (HexagonalDirection.SOUTHWEST, HexagonalCoordinates(10, 19)),
        (HexagonalDirection.SOUTHEAST, HexagonalCoordinates(11, 19)),
    ],
)
def test_hexagonal_coordinates_can_be_moved(direction, expected):
    p = HexagonalCoordinates(east=10, northeast=20)
    assert p.move(direction) == expected


def test_hexagonal_position_has_six_neighbors():
    p = HexagonalCoordinates(east=10, northeast=20)
    neighbors = list(p.neighbors())
    assert neighbors == [
        HexagonalCoordinates(11, 20),
        HexagonalCoordinates(10, 21),
        HexagonalCoordinates(9, 21),
        HexagonalCoordinates(9, 20),
        HexagonalCoordinates(10, 19),
        HexagonalCoordinates(11, 19),
    ]
