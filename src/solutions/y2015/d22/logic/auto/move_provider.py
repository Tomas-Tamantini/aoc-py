from typing import Iterator

from src.solutions.y2015.d22.logic.actions.moves import GameMove
from src.solutions.y2015.d22.logic.state.attributes import current_turn
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.game_state import GameState


class AutoMoveProvider:
    def __init__(
        self, player_moves: list[GameMove], boss_moves: list[GameMove]
    ):
        self._moves = {
            Character.PLAYER: player_moves,
            Character.BOSS: boss_moves,
        }

    def next_moves(self, game_state: GameState) -> Iterator[GameMove]:
        for move in self._moves[current_turn(game_state)]:
            if move.is_valid(game_state):
                yield move
