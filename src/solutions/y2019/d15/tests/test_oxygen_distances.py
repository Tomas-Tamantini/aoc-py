from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d15.logic.oxygen_distances import calculate_distances
from src.solutions.y2019.d15.logic.oxygen_system_area import OxygenSystemArea


def _oxygen_system_area() -> OxygenSystemArea:
    """
    #######
    #.....#
    #.....#
    #S.#.O#
    #.....#
    #.....#
    #.....#
    #######
    """
    tiles = {
        Vector2D(x, y)
        for x in range(5)
        for y in range(6)
        if (x != 2) or (y != 2)
    }
    return OxygenSystemArea(
        droid_start_position=Vector2D(0, 2),
        oxygen_system_position=Vector2D(4, 2),
        tiles=tiles,
    )


def test_oxygen_system_distances():
    area = _oxygen_system_area()
    distances = calculate_distances(area)
    assert distances.start_to_oxygen == 6
    assert distances.furthest_from_oxygen == 7
