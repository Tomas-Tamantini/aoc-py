from typing import Iterator

from src.solutions.shared.geometry.vector_2d import Vector2D


def _neighbors(
    roll_pos: Vector2D, other_rolls: set[Vector2D]
) -> Iterator[Vector2D]:
    for n in roll_pos.neighbors(include_diagonals=True):
        if n in other_rolls:
            yield n


def roll_is_reachable(roll_pos: Vector2D, other_rolls: set[Vector2D]) -> bool:
    num_neighbors = len(list(_neighbors(roll_pos, other_rolls)))
    return num_neighbors < 4


def removable_rolls(roll_positions: set[Vector2D]) -> set[Vector2D]:
    remaining = roll_positions.copy()
    rolls_to_remove = {
        r for r in roll_positions if roll_is_reachable(r, roll_positions)
    }
    while rolls_to_remove:
        roll = rolls_to_remove.pop()
        remaining.remove(roll)
        for neighbor in _neighbors(roll, remaining):
            if roll_is_reachable(neighbor, remaining):
                rolls_to_remove.add(neighbor)
    return roll_positions - remaining
