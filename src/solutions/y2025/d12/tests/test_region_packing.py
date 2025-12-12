from src.solutions.shared.geometry.vector_2d import Vector2D
from src.solutions.y2025.d12.logic.packing import Region, Shape

SHAPES = {
    0: Shape(id=0, cells={Vector2D(0, 0), Vector2D(1, 0)}),
    1: Shape(id=1, cells={Vector2D(2, 0), Vector2D(2, 1), Vector2D(2, 2)}),
}


def test_region_cannot_be_packed_if_not_enough_area():
    region = Region(width=10, height=20, shape_requirements={0: 50, 1: 34})
    # Area required = 50 * 2 + 3 * 34 = 202 > 200
    assert not region.can_be_packed(SHAPES)


def test_region_can_be_packed_if_enough_area():
    region = Region(width=10, height=20, shape_requirements={0: 50, 1: 33})
    # Area required = 50 * 2 + 3 * 33 = 198 > 200
    assert region.can_be_packed(SHAPES)
