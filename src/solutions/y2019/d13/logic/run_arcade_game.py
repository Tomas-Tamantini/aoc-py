from typing import Optional

from src.core.animation_renderer import AnimationRenderer
from src.solutions.y2019.d13.logic.arcade_io import ArcadeIO
from src.solutions.y2019.d13.logic.arcade_screen import ArcadeScreen
from src.solutions.y2019.intcode import IntcodeProgram, run_intcode_program


def run_arcade_game(
    screen: ArcadeScreen,
    instructions: list[int],
    animation_renderer: Optional[AnimationRenderer] = None,
) -> None:
    io = ArcadeIO(screen, animation_renderer)
    program = IntcodeProgram(instructions)
    run_intcode_program(program, serial_output=io, serial_input=io)
