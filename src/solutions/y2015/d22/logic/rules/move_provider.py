from typing import Iterator, Protocol

from src.solutions.y2015.d22.logic.actions.moves import GameMove
from src.solutions.y2015.d22.logic.state.game_state import GameState


class MoveProvider(Protocol):
    def next_moves(self, game_state: GameState) -> Iterator[GameMove]: ...
