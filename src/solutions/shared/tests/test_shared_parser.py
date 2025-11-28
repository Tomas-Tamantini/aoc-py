import pytest

from src.solutions.shared.geometry import Vector2D
from src.solutions.shared.parser import parse_csv, parse_grid


def test_csv_parser_uses_comma_as_default_separator(input_reader):
    reader = input_reader("1, 2\n3, 4\n 5,6 \n \t")
    values = list(parse_csv(reader))
    assert values == [("1", "2"), ("3", "4"), ("5", "6")]


def test_csv_parser_can_receive_custom_mapper(input_reader):
    reader = input_reader("1: 2\n3: 4\n 5:6 \n \t")
    values = list(
        parse_csv(
            reader,
            separator=":",
            mapper=lambda values: Vector2D(*map(int, values)),
        )
    )
    assert values == [Vector2D(1, 2), Vector2D(3, 4), Vector2D(5, 6)]


@pytest.fixture
def reader(input_reader):
    return input_reader(
        """
        .#.
        O#.
        """
    )


@pytest.fixture
def grid(reader):
    return parse_grid(reader)


def test_character_grid_stores_dimensions(grid):
    assert grid.width == 3
    assert grid.height == 2


def test_character_grid_allows_position_lookup(grid):
    assert grid.symbol_at(Vector2D(0, 0)) == "."
    assert grid.symbol_at(Vector2D(1, 0)) == "#"
    assert grid.symbol_at(Vector2D(0, 1)) == "O"


def test_character_grid_allows_symbol_lookup(grid):
    assert grid.positions("#") == {Vector2D(1, 0), Vector2D(1, 1)}
    assert grid.positions("O") == {Vector2D(0, 1)}


def test_grid_parser_allows_mirroring_y_coords(reader):
    grid = parse_grid(reader, y_grows_down=False)
    assert grid.symbol_at(Vector2D(0, 0)) == "O"
    assert grid.symbol_at(Vector2D(1, 0)) == "#"
    assert grid.symbol_at(Vector2D(0, 1)) == "."
