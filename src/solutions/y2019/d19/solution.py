from typing import Iterator, Optional

from src.core.animation_renderer import AnimationRenderer
from src.core.io_handler import IOHandler
from src.core.progress_monitor import ProgressMonitor
from src.solutions.shared.geometry.vector_2d import Vector2D
from src.solutions.y2019.d19.logic.beam_sensor import BeamSensor
from src.solutions.y2019.d19.logic.closest_square import closest_square
from src.solutions.y2019.intcode import parse_instructions


def _positions_inside_beam(
    area_size: int,
    sensor: BeamSensor,
    progress_monitor: ProgressMonitor,
    animation_renderer: Optional[AnimationRenderer] = None,
) -> Iterator[Vector2D]:
    frame = ""
    for y in range(area_size):
        if not animation_renderer:
            progress_monitor.update_progress_bar(
                current_step=y + 1, total_steps=area_size
            )
        for x in range(area_size):
            pos = Vector2D(x, y)
            if sensor.is_inside_beam(pos):
                yield pos
            if animation_renderer:
                char = "#" if sensor.is_inside_beam(pos) else "."
                frame += char
                animation_renderer.render_frame(frame, fps=240)
        frame += "\n"


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 19
    instructions = parse_instructions(io_handler.input_reader(*prob_id))

    sensor = BeamSensor(instructions)

    positions_in_beam = _positions_inside_beam(
        area_size=50,
        sensor=sensor,
        progress_monitor=io_handler.progress_monitor(*prob_id, part=1),
        animation_renderer=io_handler.animation_renderer(*prob_id, part=1),
    )
    num_pos = len(set(positions_in_beam))

    io_handler.write_result(
        *prob_id, part=1, result=num_pos, supports_animation=True
    )

    square_pos = closest_square(square_size=100, beam_sensor=sensor)
    io_handler.write_result(
        *prob_id, part=2, result=10000 * square_pos.x + square_pos.y
    )
