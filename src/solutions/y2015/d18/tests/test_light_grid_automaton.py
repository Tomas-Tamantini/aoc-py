import pytest

from src.solutions.shared.parser.grid_parser import parse_grid
from src.solutions.y2015.d18.logic.light_grid_automaton import (
    LightGridAutomaton,
)


@pytest.fixture
def light_grid(input_reader):
    def _light_grid(grid: str, stuck_lights: bool) -> LightGridAutomaton:
        chr_grid = parse_grid(input_reader(grid))
        return LightGridAutomaton(
            width=chr_grid.width,
            height=chr_grid.height,
            alive_cells=chr_grid.positions("#"),
            corner_lights_always_on=stuck_lights,
        )

    return _light_grid


def test_light_grid_automaton_iterates_without_stuck_corner_lights(light_grid):
    grid_str = "\n".join(
        [
            ".#.#.#",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            "####..",
        ]
    )
    grid = light_grid(grid_str, stuck_lights=False)
    num_live_cells = [len(grid.alive_cells())]
    for _ in range(4):
        grid = grid.next_iteration()
        num_live_cells.append(len(grid.alive_cells()))
    assert num_live_cells == [15, 11, 8, 4, 4]


def test_light_grid_automaton_iterates_with_stuck_corner_lights(light_grid):
    grid_str = "\n".join(
        [
            ".#.#..",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            ".###..",
        ]
    )
    grid = light_grid(grid_str, stuck_lights=True)
    num_live_cells = [len(grid.alive_cells())]
    for _ in range(5):
        grid = grid.next_iteration()
        num_live_cells.append(len(grid.alive_cells()))
    assert num_live_cells == [17, 18, 18, 18, 14, 17]
