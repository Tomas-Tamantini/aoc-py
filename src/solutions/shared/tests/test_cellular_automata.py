import pytest

from src.solutions.shared.cellular_automata.game_of_life import GameOfLife
from src.solutions.shared.cellular_automata.wireworld import (
    WireWorld,
    WireWorldState,
)
from src.solutions.shared.geometry import Vector2D


@pytest.fixture
def wireworld() -> WireWorld:
    cells = dict()
    for x in range(3):
        cells[Vector2D(x, 0)] = WireWorldState.ELECTRON_TAIL
        cells[Vector2D(x, 1)] = WireWorldState.ELECTRON_HEAD
        cells[Vector2D(x, 2)] = WireWorldState.CONDUCTOR
    return WireWorld(cells)


def test_multi_state_cellular_automaton_iterates(wireworld):
    next_iteration = wireworld.next_iteration()
    expected_cells = {
        Vector2D(0, 0): WireWorldState.CONDUCTOR,
        Vector2D(0, 1): WireWorldState.ELECTRON_TAIL,
        Vector2D(0, 2): WireWorldState.ELECTRON_HEAD,
        Vector2D(1, 0): WireWorldState.CONDUCTOR,
        Vector2D(1, 1): WireWorldState.ELECTRON_TAIL,
        Vector2D(1, 2): WireWorldState.CONDUCTOR,
        Vector2D(2, 0): WireWorldState.CONDUCTOR,
        Vector2D(2, 1): WireWorldState.ELECTRON_TAIL,
        Vector2D(2, 2): WireWorldState.ELECTRON_HEAD,
    }
    assert next_iteration.cells == expected_cells


@pytest.fixture
def game_of_life() -> GameOfLife:
    return GameOfLife(
        alive_cells={
            Vector2D(0, 0),
            Vector2D(0, 1),
            Vector2D(0, 2),
            Vector2D(1, 2),
            Vector2D(2, 1),
        }
    )


def test_binary_cellular_automaton_iterates(game_of_life):
    expected_live_cells = {
        Vector2D(-1, 1),
        Vector2D(0, 1),
        Vector2D(0, 2),
        Vector2D(1, 0),
        Vector2D(1, 2),
    }
    next_iteration = game_of_life.next_iteration()
    assert next_iteration.alive_cells() == expected_live_cells
