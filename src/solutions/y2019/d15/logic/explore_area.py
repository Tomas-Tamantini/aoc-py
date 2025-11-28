from typing import Optional

from src.core.animation_renderer import AnimationRenderer
from src.solutions.shared.geometry import Direction, Vector2D
from src.solutions.y2019.d15.logic.animate_repair_droid import (
    build_repair_droid_frame,
)
from src.solutions.y2019.d15.logic.droid_controller import DroidController
from src.solutions.y2019.d15.logic.oxygen_system_area import OxygenSystemArea
from src.solutions.y2019.d15.logic.repair_droid_io import RepairDroidIO


def _next_direction_to_explore(
    droid_position: Vector2D, explored_positions: set[Vector2D]
) -> Optional[Direction]:
    for direction in Direction:
        next_pos = droid_position.move(direction)
        if next_pos not in explored_positions:
            return direction


def explore_oxygem_system_area(
    droid_io: RepairDroidIO,
    animation_renderer: Optional[AnimationRenderer] = None,
) -> OxygenSystemArea:
    droid_controller = DroidController(droid_io)
    tiles = {droid_controller.droid_start_position}
    explored = {droid_controller.droid_start_position}
    while True:
        current_pos = droid_controller.current_droid_position
        if next_direction := _next_direction_to_explore(current_pos, explored):
            explored.add(current_pos.move(next_direction))
            droid_controller.try_move(next_direction)
            tiles.add(droid_controller.current_droid_position)
        elif droid_controller.can_backtrack():
            droid_controller.backtrack()
        else:
            break
        if animation_renderer:
            frame = build_repair_droid_frame(tiles, explored, droid_controller)
            animation_renderer.render_frame(frame, fps=60)

    return OxygenSystemArea(
        droid_start_position=droid_controller.droid_start_position,
        oxygen_system_position=droid_controller.oxygen_system_position,
        tiles=tiles,
    )
