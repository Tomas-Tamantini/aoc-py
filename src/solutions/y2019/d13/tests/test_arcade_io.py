from src.solutions.shared.geometry import Vector2D
from src.solutions.y2019.d13.logic.arcade_io import ArcadeIO
from src.solutions.y2019.d13.logic.arcade_screen import ArcadeScreen
from src.solutions.y2019.d13.logic.tile_type import TileType


def test_arcade_io_uses_every_3_inputs_to_paint_screen():
    screen = ArcadeScreen()
    io = ArcadeIO(screen)
    triplets = [
        (1, 2, 3),  # x=1, y=2, tile=PADDLE
        (2, 4, 0),  # x=2, y=4, tile=EMPTY
        (2, 4, 1),  # x=2, y=4, tile=WALL
        (2, 5, 1),  # x=2, y=5, tile=WALL
        (3, 5, 2),  # x=3, y=5, tile=BLOCK
        (4, 5, 2),  # x=4, y=5, tile=BLOCK
        (4, 4, 2),  # x=4, y=4, tile=BLOCK
        (3, 3, 4),  # x=3, y=3, tile=BALL
    ]
    for triplet in triplets:
        for output in triplet:
            io.put(output)
    assert screen.num_tiles(TileType.PADDLE) == 1
    assert screen.num_tiles(TileType.WALL) == 2
    assert screen.num_tiles(TileType.BLOCK) == 3
    assert screen.num_tiles(TileType.BALL) == 1


def test_arcade_io_uses_special_input_to_update_score():
    screen = ArcadeScreen()
    io = ArcadeIO(screen)
    triplet = (-1, 0, 12345)
    for output in triplet:
        io.put(output)
    assert screen.score == 12345


def test_arcade_io_should_not_move_paddle_if_aligned_with_the_ball():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(3, 0), tile_type=TileType.PADDLE)
    screen.set_tile(position=Vector2D(3, 9), tile_type=TileType.BALL)
    io = ArcadeIO(screen)
    assert io.read_next() == 0


def test_arcade_io_should_move_paddle_right_if_ball_is_to_the_right():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(3, 0), tile_type=TileType.PADDLE)
    screen.set_tile(position=Vector2D(5, 9), tile_type=TileType.BALL)
    io = ArcadeIO(screen)
    assert io.read_next() == 1


def test_arcade_io_should_move_paddle_left_if_ball_is_to_the_left():
    screen = ArcadeScreen()
    screen.set_tile(position=Vector2D(3, 0), tile_type=TileType.PADDLE)
    screen.set_tile(position=Vector2D(1, 9), tile_type=TileType.BALL)
    io = ArcadeIO(screen)
    assert io.read_next() == -1
