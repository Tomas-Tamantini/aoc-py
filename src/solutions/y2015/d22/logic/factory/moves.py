from typing import Optional

from src.core.game_interface import GameInterface
from src.solutions.y2015.d22.logic.actions.moves import (
    DirectDamage,
    Drain,
    GameMove,
    MagicMissile,
    Poison,
    Recharge,
    Shield,
)
from src.solutions.y2015.d22.logic.auto.move_provider import AutoMoveProvider
from src.solutions.y2015.d22.logic.interactive.move_provider import (
    InteractiveMoveProvider,
)
from src.solutions.y2015.d22.logic.rules.move_provider import MoveProvider


def player_moves() -> list[GameMove]:
    return [MagicMissile(), Drain(), Shield(), Poison(), Recharge()]


def boss_moves(damage: int) -> list[GameMove]:
    return [DirectDamage(damage=damage)]


def build_move_provider(
    boss_damage: int, game_interface: Optional[GameInterface]
) -> MoveProvider:
    if game_interface:
        return InteractiveMoveProvider(
            player_moves=player_moves(),
            boss_move=boss_moves(boss_damage)[0],
            game_interface=game_interface,
        )
    else:
        return AutoMoveProvider(player_moves(), boss_moves(boss_damage))
