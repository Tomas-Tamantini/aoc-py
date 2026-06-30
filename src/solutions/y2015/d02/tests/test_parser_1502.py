from src.solutions.y2015.d02.logic.parser import parse_rectangular_boxes
from src.solutions.y2015.d02.logic.rectangular_box import RectangularBox


def test_parse_rectangular_boxes(input_reader):
    reader = input_reader("""2x3x4
                             1x1x10""")
    boxes = list(parse_rectangular_boxes(reader))
    assert boxes == [
        RectangularBox(length=2, width=3, height=4),
        RectangularBox(length=1, width=1, height=10),
    ]
