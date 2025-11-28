from typing import Optional

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d15.logic.repair_droid_io import RepairDroidIO


class DroidController:
    def __init__(self, droid_io: RepairDroidIO) -> None:
        self._droid_io = droid_io
        self._oxygen_system_position: Optional[Vector2D] = None
        self._position_history = [Vector2D(0, 0)]

    @property
    def current_droid_position(self) -> Vector2D:
        return self._position_history[-1]

    @property
    def droid_start_position(self) -> Vector2D:
        return self._position_history[0]

    @property
    def oxygen_system_position(self) -> Vector2D:
        if not self._oxygen_system_position:
            raise ValueError("Could not find oxygen system position")
        return self._oxygen_system_position

    def try_move(self, direction: Direction) -> None:
        move_output = self._droid_io.try_move(direction)
        if move_output.hit_wall:
            return
        next_pos = self.current_droid_position.move(direction)
        self._position_history.append(next_pos)
        if move_output.found_oxygen_system:
            self._oxygen_system_position = next_pos

    def can_backtrack(self) -> bool:
        return len(self._position_history) > 1

    def _backtrack_direction(self) -> Direction:
        diff = self._position_history[-2] - self._position_history[-1]
        if diff.x == 1:
            return Direction.RIGHT
        elif diff.x == -1:
            return Direction.LEFT
        elif diff.y == 1:
            return Direction.UP
        else:
            return Direction.DOWN

    def backtrack(self) -> None:
        self._droid_io.try_move(self._backtrack_direction())
        self._position_history.pop()
