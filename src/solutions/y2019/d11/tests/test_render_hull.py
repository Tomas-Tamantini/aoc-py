from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d11.logic.hull import Hull
from src.solutions.y2019.d11.logic.render_hull import render_hull


def test_render_hull():
    hull = Hull()
    hull.paint_panel(Vector2D(100, 200), paint_white=True)
    hull.paint_panel(Vector2D(101, 200), paint_white=True)
    hull.paint_panel(Vector2D(102, 201), paint_white=True)
    assert render_hull(hull) == "\n  #\n## "
