from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2022.d09.logic.pull_motion import PullMotion, apply_motions


def test_rope_starts_with_all_knots_at_origin():
    rope = next(apply_motions(num_knots=3, motions=[]))
    assert rope.knots_head_to_tail == 3 * (Vector2D(0, 0),)


def test_pull_motions_are_applied_in_succession():
    *_, last_rope = apply_motions(
        num_knots=3,
        motions=[
            PullMotion(Direction.RIGHT, 5),
            PullMotion(Direction.DOWN, 3),
        ],
    )
    assert last_rope.tail == Vector2D(4, -1)
