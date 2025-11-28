from dataclasses import replace

import pytest

from src.solutions.y2015.d22.logic.actions.atomic import (
    AddTimedEffect,
    DealDamage,
    DecrementEffectTimer,
    Heal,
    IncrementEffectPointer,
    RechargeMana,
    RemoveEffect,
    ResetEffectPointer,
    SpendMana,
    ToggleTurn,
)
from src.solutions.y2015.d22.logic.state.attributes import (
    hit_points,
    mana_points,
)
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import ShieldEffect


def test_toggle_turn_increments_character_idx(initial_state):
    transformation = ToggleTurn()
    state = transformation.apply(initial_state)
    assert state.next_character_idx == 1
    state = transformation.apply(state)
    assert state.next_character_idx == 0


def test_increment_effect_pointer_increments_idx(initial_state):
    transformation = IncrementEffectPointer()
    state = transformation.apply(initial_state)
    assert state.next_effect_idx == 1


def test_reset_effect_pointer_sets_pointer_to_zero(poison_state):
    transformation = ResetEffectPointer()
    state = transformation.apply(poison_state)
    assert state.next_effect_idx == 0


def test_decrement_effect_timer_decrements_current_timer(poison_state):
    transformation = DecrementEffectTimer()
    state = transformation.apply(poison_state)
    assert state.active_effects[1].timer == 3


def test_remove_effect_removes_from_list(recharge_state):
    transformation = RemoveEffect()
    state = transformation.apply(recharge_state)
    assert len(state.active_effects) == len(recharge_state.active_effects) - 1


def test_add_effect_appends_to_end_of_list(initial_state, poison_effect):
    transformation = AddTimedEffect(poison_effect, duration=6)
    state = transformation.apply(initial_state)
    assert state.active_effects == (
        EffectState(effect=poison_effect, timer=6),
    )


def test_recharge_mana_increments_mana_points(initial_state):
    transformation = RechargeMana(target=Character.PLAYER, recharge_amount=101)
    state = transformation.apply(initial_state)
    assert mana_points(state, Character.PLAYER) == 601


def test_spend_mana_decrements_mana_points(initial_state):
    transformation = SpendMana(target=Character.PLAYER, mana_cost=101)
    state = transformation.apply(initial_state)
    assert mana_points(state, Character.PLAYER) == 399


def test_heal_increments_hit_points(initial_state):
    transformation = Heal(target=Character.PLAYER, hit_points_increment=2)
    state = transformation.apply(initial_state)
    assert hit_points(state, Character.PLAYER) == 52


@pytest.fixture
def state_with_armor(initial_state):
    def _state(armor: int):
        return replace(
            initial_state,
            active_effects=(
                EffectState(
                    effect=ShieldEffect(target=Character.PLAYER, armor=armor),
                    timer=1,
                ),
            ),
        )

    return _state


@pytest.mark.parametrize(("armor", "hp"), [(0, 37), (10, 47), (20, 49)])
def test_deal_damage_deals_damage_minus_armor(state_with_armor, armor, hp):
    transformation = DealDamage(target=Character.PLAYER, damage=13)
    state = transformation.apply(state_with_armor(armor))
    assert hit_points(state, Character.PLAYER) == hp
