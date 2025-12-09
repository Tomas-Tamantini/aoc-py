from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d09.logic.rectangle import Rectangle


def test_rectangle_area_is_calculated_from_opposite_corners():
    r = Rectangle(corner_a=Vector2D(10, 20), corner_b=Vector2D(7, 24))
    assert r.area == 20
