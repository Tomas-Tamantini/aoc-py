from typing import Protocol

from src.solutions.y2015.d22.logic.state.game_state import GameState


class GameAction(Protocol):
    @property
    def mana_cost(self) -> int: ...

    def apply(self, game_state: GameState) -> GameState: ...
