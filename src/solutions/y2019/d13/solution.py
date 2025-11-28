from src.core.io_handler import IOHandler
from src.solutions.y2019.d13.logic.arcade_screen import ArcadeScreen
from src.solutions.y2019.d13.logic.run_arcade_game import run_arcade_game
from src.solutions.y2019.d13.logic.tile_type import TileType
from src.solutions.y2019.intcode import parse_instructions


def solve(io_handler: IOHandler) -> None:
    prob_id = 2019, 13
    instructions = parse_instructions(io_handler.input_reader(*prob_id))

    screen = ArcadeScreen()
    run_arcade_game(screen, instructions)
    num_blocks = screen.num_tiles(TileType.BLOCK)
    io_handler.write_result(*prob_id, part=1, result=num_blocks)

    modified_instructions = instructions[:]
    modified_instructions[0] = 2
    animation_renderer = io_handler.animation_renderer(*prob_id, part=2)
    screen = ArcadeScreen()
    run_arcade_game(screen, modified_instructions, animation_renderer)
    io_handler.write_result(
        *prob_id, part=2, result=screen.score, supports_animation=True
    )
