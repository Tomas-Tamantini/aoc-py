from src.solutions.shared.geometry import HexagonalCoordinates
from src.solutions.y2020.d24.logic.hexagonal_automaton import (
    HexagonalAutomaton,
)


def test_hexagonal_automaton_iterates():
    black_tiles = {HexagonalCoordinates(0, 0), HexagonalCoordinates(1, 0)}
    automaton = HexagonalAutomaton(black_tiles)
    automaton = automaton.next_iteration()
    assert automaton.num_black_tiles() == 4
    automaton = automaton.next_iteration()
    assert automaton.num_black_tiles() == 6
    automaton = automaton.next_iteration()
    assert automaton.num_black_tiles() == 12
