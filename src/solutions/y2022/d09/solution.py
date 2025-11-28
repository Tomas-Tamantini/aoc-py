from src.core.io_handler import IOHandler
from src.solutions.shared.geometry import Vector2D
from src.solutions.y2022.d09.logic.animation import RopeAnimation
from src.solutions.y2022.d09.logic.parser import parse_pull_motions
from src.solutions.y2022.d09.logic.pull_motion import apply_motions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2022, 9

    motions = list(parse_pull_motions(io_handler.input_reader(*prob_id)))
    total_steps = sum(m.num_steps for m in motions)

    visited: set[Vector2D] = set()
    for rope in apply_motions(num_knots=2, motions=motions):
        visited.add(rope.tail)
    io_handler.write_result(*prob_id, part=1, result=len(visited))

    animation_renderer = io_handler.animation_renderer(*prob_id, part=2)
    animation = RopeAnimation(num_frames=total_steps)
    visited = set()
    for rope in apply_motions(num_knots=10, motions=motions):
        visited.add(rope.tail)
        if animation_renderer:
            frame = animation.build_frame(rope)
            animation_renderer.render_frame(frame, fps=20)
    io_handler.write_result(
        *prob_id, part=2, result=len(visited), supports_animation=True
    )
