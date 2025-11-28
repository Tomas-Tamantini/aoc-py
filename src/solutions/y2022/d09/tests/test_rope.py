from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2022.d09.logic.rope import Rope, pull_rope


def test_pulling_empty_rope_returns_empty_rope():
    empty_rope = Rope(knots_head_to_tail=tuple())
    rope_after = pull_rope(empty_rope, Direction.UP)
    assert rope_after == empty_rope


def test_pulling_rope_obeys_rope_physics():
    rope_before = Rope(
        knots_head_to_tail=(
            Vector2D(2, 2),
            Vector2D(2, 1),
            Vector2D(1, 0),
            Vector2D(1, 0),
            Vector2D(0, 0),
        )
    )
    rope_after = pull_rope(rope_before, Direction.UP)
    assert rope_after == Rope(
        knots_head_to_tail=(
            Vector2D(2, 3),
            Vector2D(2, 2),
            Vector2D(2, 1),
            Vector2D(1, 0),
            Vector2D(0, 0),
        )
    )
