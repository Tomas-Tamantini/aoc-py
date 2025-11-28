from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d11.logic.hull import Hull


def test_hull_starts_empty():
    hull = Hull()
    assert hull.num_panels_painted_at_least_once == 0


def test_hull_keeps_track_of_panels_painted_at_least_once():
    hull = Hull()
    hull.paint_panel(position=Vector2D(10, 20), paint_white=True)
    hull.paint_panel(position=Vector2D(10, 20), paint_white=False)
    hull.paint_panel(position=Vector2D(20, 20), paint_white=False)
    assert hull.num_panels_painted_at_least_once == 2


def test_hull_keeps_track_of_white_panels():
    hull = Hull()
    hull.paint_panel(Vector2D(100, 200), paint_white=True)
    hull.paint_panel(Vector2D(101, 200), paint_white=True)
    hull.paint_panel(Vector2D(102, 201), paint_white=True)
    # Paint same panel white, then black - should not render
    hull.paint_panel(Vector2D(102, 202), paint_white=True)
    hull.paint_panel(Vector2D(102, 202), paint_white=False)
    assert hull.white_panels == {
        Vector2D(100, 200),
        Vector2D(101, 200),
        Vector2D(102, 201),
    }
