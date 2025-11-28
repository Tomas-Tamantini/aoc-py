from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d15.logic.explore_area import (
    explore_oxygem_system_area,
)
from src.solutions.y2019.d15.logic.repair_droid_io import DroidOutputInfo


class _MockDroidIO:
    """
    #########
    #S....#.#
    #.....#.#
    #.......#
    #.....#.#
    #.....#O#
    #########
    """

    def __init__(self) -> None:
        self._droid_position = Vector2D(0, 0)
        self._oxygen_position = Vector2D(6, 4)

    def _is_wall(self, pos: Vector2D) -> bool:
        if (
            pos.x < 0
            or pos.x > self._oxygen_position.x
            or pos.y < 0
            or pos.y > self._oxygen_position.y
        ):
            return True
        wall_positions = {Vector2D(5, y) for y in (0, 1, 3, 4)}
        return pos in wall_positions

    def try_move(self, direction: Direction) -> DroidOutputInfo:
        next_pos = self._droid_position.move(direction)
        if self._is_wall(next_pos):
            return DroidOutputInfo(hit_wall=True, found_oxygen_system=False)
        else:
            self._droid_position = next_pos
            return DroidOutputInfo(
                hit_wall=False,
                found_oxygen_system=(next_pos == self._oxygen_position),
            )


def test_oxygen_system_area_gets_fully_explored():
    droid_io = _MockDroidIO()
    area = explore_oxygem_system_area(droid_io)
    assert area.droid_start_position == Vector2D(0, 0)
    assert area.oxygen_system_position == Vector2D(6, 4)
    assert len(area.tiles) == 31
