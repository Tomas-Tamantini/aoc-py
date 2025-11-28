from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d13.logic.arcade_screen import ArcadeScreen
from src.solutions.y2019.d13.logic.tile_type import TileType


def test_arcade_screen_starts_empty():
    screen = ArcadeScreen()
    assert screen.num_tiles(TileType.BLOCK) == 0
    assert screen.num_tiles(TileType.WALL) == 0
    assert screen.num_tiles(TileType.PADDLE) == 0
    assert screen.num_tiles(TileType.BALL) == 0


def test_arcade_screen_allows_setting_tiles():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(1, 2), tile_type=TileType.BLOCK)
    screen.set_tile(position=Vector2D(2, 2), tile_type=TileType.BLOCK)
    screen.set_tile(position=Vector2D(3, 2), tile_type=TileType.WALL)
    assert screen.num_tiles(TileType.BLOCK) == 2
    assert screen.num_tiles(TileType.WALL) == 1


def test_arcade_screen_allows_overwriting_tiles():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(1, 2), tile_type=TileType.BLOCK)
    screen.set_tile(position=Vector2D(1, 2), tile_type=TileType.WALL)
    assert screen.num_tiles(TileType.BLOCK) == 0
    assert screen.num_tiles(TileType.WALL) == 1


def test_arcade_screen_allows_setting_score():
    screen = ArcadeScreen()
    screen.set_score(123)
    assert screen.score == 123


def test_can_query_ball_and_paddle_positions():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(1, 2), tile_type=TileType.PADDLE)
    screen.set_tile(position=Vector2D(3, 4), tile_type=TileType.BALL)
    assert screen.paddle_position() == Vector2D(1, 2)
    assert screen.ball_position() == Vector2D(3, 4)
