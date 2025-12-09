from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d09.logic.rectangle_finder import RectangleFinder

VERTICES = [
    Vector2D(7, 1),
    Vector2D(11, 1),
    Vector2D(11, 7),
    Vector2D(9, 7),
    Vector2D(9, 5),
    Vector2D(2, 5),
    Vector2D(2, 3),
    Vector2D(7, 3),
]


def test_rectangle_finder_finds_largest_rectangle():
    finder = RectangleFinder(VERTICES)
    assert finder.largest_rectangle_area() == 50


def test_rectangle_finder_finds_largest_inscribed_rectangle():
    finder = RectangleFinder(VERTICES)
    assert finder.largest_inscribed_rectangle_area() == 24
