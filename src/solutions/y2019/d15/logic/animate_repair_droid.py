from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2019.d15.logic.droid_controller import DroidController


def _tile_character(
    pos: Vector2D,
    explored_tiles: set[Vector2D],
    empty_tiles: set[Vector2D],
    droid_controller: DroidController,
) -> str:
    if pos == droid_controller._oxygen_system_position:
        return "O"
    elif pos == droid_controller.droid_start_position:
        return "S"
    elif pos == droid_controller.current_droid_position:
        return "D"
    elif pos in empty_tiles:
        return "."
    elif pos in explored_tiles:
        return "#"
    else:
        return " "


def build_repair_droid_frame(
    empty_tiles: set[Vector2D],
    explored_tiles: set[Vector2D],
    droid_controller: DroidController,
) -> str:
    bb = BoundingBox(explored_tiles)
    lines = []
    for y in range(bb.min_y, bb.max_y + 1):
        row_tiles = []
        for x in range(bb.min_x, bb.max_x + 1):
            pos = Vector2D(x, y)
            row_tiles.append(
                _tile_character(
                    pos, explored_tiles, empty_tiles, droid_controller
                )
            )
        lines.append("".join(row_tiles))
    return "\n".join(lines)
