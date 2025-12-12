import pytest

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2025.d12.logic.packing import Region, Shape
from src.solutions.y2025.d12.logic.parser import (
    parse_packing_regions,
    parse_shapes,
)


@pytest.fixture
def reader(input_reader):
    return input_reader(
        """
        0:
        #..
        .#.
        #..

        1:
        ...
        #..
        ..#

        4x4: 0 0 0 0 2 0
        12x5: 1 0 1 0 2 2
        """
    )


def test_parse_shapes(reader):
    assert list(parse_shapes(reader)) == [
        Shape(id=0, cells={Vector2D(0, 0), Vector2D(1, 1), Vector2D(0, 2)}),
        Shape(id=1, cells={Vector2D(0, 1), Vector2D(2, 2)}),
    ]


def test_parse_packing_regions(reader):
    assert list(parse_packing_regions(reader)) == [
        Region(width=4, height=4, shape_requirements={4: 2}),
        Region(
            width=12, height=5, shape_requirements={0: 1, 2: 1, 4: 2, 5: 2}
        ),
    ]
