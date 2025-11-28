from typing import Iterator

from src.core.game_interface import GameInterface
from src.solutions.y2015.d22.logic.actions.moves import GameMove
from src.solutions.y2015.d22.logic.interactive.to_str import (
    move_name,
    move_to_str,
)
from src.solutions.y2015.d22.logic.state.attributes import current_turn
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.game_state import GameState


class InteractiveMoveProvider:
    def __init__(
        self,
        player_moves: list[GameMove],
        boss_move: GameMove,
        game_interface: GameInterface,
    ):
        self._boss_move = boss_move
        self._player_moves = player_moves
        self._game_interface = game_interface
        self._delay_ms = 50

    @staticmethod
    def _move_menu(available_moves: list[GameMove]) -> str:
        menu_options = []
        for m in available_moves:
            name = move_name(m)
            menu_options.append(
                f" {name[0].lower()}: {name} ({m.action().mana_cost} mana)"
            )
        return "Select a move:\n" + "\n".join(menu_options)

    def _select_move(self, available_moves: list[GameMove]) -> GameMove:
        while True:
            self._game_interface.put_string(
                self._move_menu(available_moves), delay_ms=self._delay_ms
            )
            self._game_interface.put_character("> ")
            user_input = self._game_interface.prompt_input().strip().upper()
            if not user_input:
                self._game_interface.put_string("Invalid move", self._delay_ms)
            for move in available_moves:
                if move_name(move)[0] == user_input:
                    return move
            self._game_interface.put_string("Invalid move", self._delay_ms)

    def next_moves(self, game_state: GameState) -> Iterator[GameMove]:
        if current_turn(game_state) == Character.BOSS:
            move = self._boss_move
        elif available_moves := [
            m for m in self._player_moves if m.is_valid(game_state)
        ]:
            move = self._select_move(available_moves)
        else:
            return
        self._game_interface.put_string(
            move_to_str(move, game_state), self._delay_ms
        )
        yield move
