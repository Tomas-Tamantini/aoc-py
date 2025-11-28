from dataclasses import replace

from src.solutions.y2015.d22.logic.actions.moves import (
    Drain,
    MagicMissile,
    Poison,
    Shield,
)
from src.solutions.y2015.d22.logic.state.effect_state import EffectState


def test_auto_move_provider_yields_moves_for_current_character(
    initial_state, move_provider, player_moves, boss_moves
):
    moves = list(move_provider.next_moves(initial_state))
    assert moves == player_moves

    boss_turn = replace(initial_state, next_character_idx=1)
    moves = list(move_provider.next_moves(boss_turn))
    assert moves == boss_moves


def test_auto_move_provider_yields_only_moves_with_sufficient_mana(
    initial_state, move_provider
):
    state = replace(
        initial_state,
        characters=(
            replace(initial_state.characters[0], mana_points=113),
            initial_state.characters[1],
        ),
    )
    moves = list(move_provider.next_moves(state))
    assert moves == [MagicMissile(), Drain(), Shield()]


def test_auto_move_provider_yields_only_moves_without_active_effects(
    initial_state, move_provider, hard_mode_effect, recharge_effect
):
    state = replace(
        initial_state,
        active_effects=[
            EffectState(effect=hard_mode_effect),
            EffectState(effect=recharge_effect),
        ],
    )
    moves = list(move_provider.next_moves(state))
    assert moves == [MagicMissile(), Drain(), Shield(), Poison()]
