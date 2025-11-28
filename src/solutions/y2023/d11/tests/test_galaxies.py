import pytest

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2023.d11.logic.galaxies import Galaxies

_positions = {
    Vector2D(0, 0),
    Vector2D(1, 1),
    Vector2D(3, 4),
}
_galaxies = Galaxies(_positions)


def test_galaxies_keep_track_of_positions():
    assert set(_galaxies.positions()) == _positions


@pytest.mark.parametrize(
    ("pos_a", "pos_b", "expected"),
    [
        (Vector2D(0, 0), Vector2D(1, 1), 2),
        (Vector2D(3, 4), Vector2D(1, 1), 3000002),
    ],
)
def test_distance_between_galaxies(pos_a, pos_b, expected):
    dist = _galaxies.distance(pos_a, pos_b, expansion_rate=1_000_000)
    assert dist == expected
