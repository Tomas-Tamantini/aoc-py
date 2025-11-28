from src.solutions.shared.geometry import HexagonalDirection
from src.solutions.y2020.d24.logic.direction_parser import (
    parse_hexagonal_directions,
)


def test_parse_hexagonal_directions(input_reader):
    reader = input_reader(
        """
        wenw
        neesesw
        """
    )
    directions = list(parse_hexagonal_directions(reader))
    assert directions == [
        [
            HexagonalDirection.WEST,
            HexagonalDirection.EAST,
            HexagonalDirection.NORTHWEST,
        ],
        [
            HexagonalDirection.NORTHEAST,
            HexagonalDirection.EAST,
            HexagonalDirection.SOUTHEAST,
            HexagonalDirection.SOUTHWEST,
        ],
    ]
