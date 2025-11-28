from src.solutions.y2015.d22.logic.actions.atomic import (
    DealDamage,
    IncrementEffectPointer,
)
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.actions.moves import (
    Drain,
    MagicMissile,
    Poison,
    Recharge,
    Shield,
)
from src.solutions.y2015.d22.logic.rules.available_actions import (
    available_actions,
)
from src.solutions.y2015.d22.logic.state.character import Character


def test_no_available_actions_if_game_is_over(
    state_with_hit_points, move_provider
):
    state = state_with_hit_points(player_hp=0, boss_hp=10)
    assert not list(available_actions(state, move_provider))


def test_available_action_in_effect_phase_is_current_effect_action(
    initial_state_hard_mode, move_provider
):
    actions = list(available_actions(initial_state_hard_mode, move_provider))
    assert len(actions) == 1
    assert actions[0] == CompositeAction(
        transformations=(
            DealDamage(target=Character.PLAYER, damage=1),
            IncrementEffectPointer(),
        )
    )


def test_available_actions_in_move_phase_are_characters_moves(
    initial_state_easy_mode, move_provider
):
    actions = list(available_actions(initial_state_easy_mode, move_provider))
    assert actions == [
        move.action()
        for move in (MagicMissile(), Drain(), Shield(), Poison(), Recharge())
    ]
