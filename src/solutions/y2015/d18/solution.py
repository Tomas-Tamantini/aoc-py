from src.core.io_handler import IOHandler
from src.core.progress_monitor import ProgressMonitor
from src.solutions.shared.parser.character_grid import CharacterGrid
from src.solutions.shared.parser.grid_parser import parse_grid
from src.solutions.y2015.d18.logic.light_grid_automaton import (
    LightGridAutomaton,
)


def _num_lights_on(
    char_grid: CharacterGrid,
    corner_lights_always_on: bool,
    progress_monitor: ProgressMonitor,
    num_steps: int = 100,
) -> int:
    grid = LightGridAutomaton(
        width=char_grid.width,
        height=char_grid.height,
        alive_cells=char_grid.positions("#"),
        corner_lights_always_on=corner_lights_always_on,
    )
    for _ in progress_monitor.track(range(num_steps)):
        grid = grid.next_iteration()
    return len(grid.alive_cells())


def solve(io_handler: IOHandler) -> None:
    prob_id = 2015, 18
    input_reader = io_handler.input_reader(*prob_id)
    chr_grid = parse_grid(input_reader)

    for part, corners_on in [(1, False), (2, True)]:
        progress_monitor = io_handler.progress_monitor(*prob_id, part=part)
        lights_on = _num_lights_on(
            chr_grid,
            corner_lights_always_on=corners_on,
            progress_monitor=progress_monitor,
        )
        io_handler.write_result(*prob_id, part=part, result=lights_on)
