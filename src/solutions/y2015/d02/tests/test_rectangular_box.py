import pytest

from src.solutions.y2015.d02.logic.rectangular_box import RectangularBox


@pytest.mark.parametrize(
    ("length", "width", "height", "expected_wrapping_paper"),
    [(2, 3, 4, 58), (1, 1, 10, 43)],
)
def test_rectangular_box_required_wrapping_paper(
    length, width, height, expected_wrapping_paper
):
    box = RectangularBox(length=length, width=width, height=height)
    assert box.required_wrapping_paper() == expected_wrapping_paper


@pytest.mark.parametrize(
    ("length", "width", "height", "expected_ribbon_length"),
    [(2, 3, 4, 34), (1, 1, 10, 14)],
)
def test_rectangular_box_required_ribbon_length(
    length, width, height, expected_ribbon_length
):
    box = RectangularBox(length=length, width=width, height=height)
    assert box.required_ribbon_length() == expected_ribbon_length
