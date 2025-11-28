from dataclasses import replace

from src.solutions.y2015.d22.logic.actions.atomic import (
    AtomicTransformation,
    DealDamage,
    DecrementEffectTimer,
    IncrementEffectPointer,
    RechargeMana,
    RemoveEffect,
)
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.rules.effect_actions import effect_action
from src.solutions.y2015.d22.logic.state.character import Character


def test_effect_actions_cost_no_mana(poison_state):
    action = effect_action(poison_state)
    assert action.mana_cost == 0


def _transformations(state) -> tuple[AtomicTransformation, ...]:
    action = effect_action(state)
    assert isinstance(action, CompositeAction)
    return action.transformations


def test_effect_runs_only_on_its_turn(hard_mode_state):
    state = replace(hard_mode_state, next_character_idx=1)
    assert not _transformations(state)[:-1]


def test_permanent_effect_increments_pointer(hard_mode_state):
    assert _transformations(hard_mode_state)[-1] == IncrementEffectPointer()


def test_timed_effect_with_remaining_time_increments_pointer(poison_state):
    assert _transformations(poison_state)[-1] == IncrementEffectPointer()


def test_timed_effect_with_remaining_time_decrements_timer(poison_state):
    assert _transformations(poison_state)[-2] == DecrementEffectTimer()


def test_timed_effect_with_no_remaining_time_gets_removed(recharge_state):
    assert _transformations(recharge_state)[-1] == RemoveEffect()


def test_hard_mode_effect_deals_damage(hard_mode_state):
    assert _transformations(hard_mode_state)[:-1] == (
        DealDamage(target=Character.PLAYER, damage=1),
    )


def test_poison_effect_deals_damage(poison_state):
    assert _transformations(poison_state)[:-2] == (
        DealDamage(target=Character.BOSS, damage=3),
    )


def test_recharge_effect_recharges_mana(recharge_state):
    assert _transformations(recharge_state)[:-1] == (
        RechargeMana(target=Character.PLAYER, recharge_amount=101),
    )
