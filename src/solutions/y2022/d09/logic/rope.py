from dataclasses import dataclass

from src.solutions.shared.geometry import Direction, Vector2D


@dataclass(frozen=True)
class Rope:
    knots_head_to_tail: tuple[Vector2D, ...]

    @property
    def head(self):
        return self.knots_head_to_tail[0]

    @property
    def tail(self):
        return self.knots_head_to_tail[-1]


def _pull_next_knot(current_knot: Vector2D, next_knot: Vector2D) -> Vector2D:
    diff = current_knot - next_knot
    if abs(diff.x) <= 1 and abs(diff.y) <= 1:
        return next_knot
    dx = diff.x // abs(diff.x) if diff.x != 0 else 0
    dy = diff.y // abs(diff.y) if diff.y != 0 else 0
    return next_knot + Vector2D(dx, dy)


def pull_rope(rope: Rope, direction: Direction) -> Rope:
    new_positions = []
    for i, knot in enumerate(rope.knots_head_to_tail):
        if i == 0:
            next_knot = knot.move(direction)
        else:
            next_knot = _pull_next_knot(new_positions[-1], knot)
        new_positions.append(next_knot)

    return Rope(tuple(new_positions))
