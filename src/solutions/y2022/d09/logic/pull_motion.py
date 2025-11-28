from dataclasses import dataclass
from typing import Iterable, Iterator

from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2022.d09.logic.rope import Rope, pull_rope


@dataclass(frozen=True)
class PullMotion:
    direction: Direction
    num_steps: int


def apply_motions(
    num_knots: int, motions: Iterable[PullMotion]
) -> Iterator[Rope]:
    initial_positions = num_knots * (Vector2D(0, 0),)
    rope = Rope(initial_positions)
    yield rope
    for motion in motions:
        for _ in range(motion.num_steps):
            rope = pull_rope(rope, motion.direction)
            yield rope
