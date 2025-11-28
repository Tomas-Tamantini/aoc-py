from typing import Iterator

from src.solutions.shared.geometry import BoundingBox, Vector2D
from src.solutions.y2019.d11.logic.hull import Hull


def _render_rows(hull: Hull) -> Iterator[str]:
    bb = BoundingBox(hull.white_panels)
    for y in range(bb.min_y, bb.max_y + 1):
        line = []
        for x in range(bb.min_x, bb.max_x + 1):
            next_chr = "#" if Vector2D(x, y) in hull.white_panels else " "
            line.append(next_chr)
        yield "".join(line)


def render_hull(hull: Hull) -> str:
    lines = list(_render_rows(hull))
    return "\n" + "\n".join(reversed(lines))
