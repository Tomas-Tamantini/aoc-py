import pytest

from src.solutions.y2015.d22.logic.actions.moves import (
    DirectDamage,
    Drain,
    MagicMissile,
    Poison,
    Recharge,
    Shield,
)
from src.solutions.y2015.d22.logic.state.attributes import (
    current_turn,
    hit_points,
    mana_points,
)
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import (
    PoisonEffect,
    RechargeEffect,
    ShieldEffect,
)


@pytest.mark.parametrize(
    "move",
    [MagicMissile(), Drain(), Shield(), Poison(), Recharge(), DirectDamage()],
)
def test_move_toggles_turn(move, initial_state):
    next_state = move.action().apply(initial_state)
    assert current_turn(next_state) == Character.BOSS


@pytest.mark.parametrize(
    "move",
    [MagicMissile(), Drain(), Shield(), Poison(), Recharge(), DirectDamage()],
)
def test_move_resets_effect_pointer(move, poison_state):
    next_state = move.action().apply(poison_state)
    assert next_state.next_effect_idx == 0


@pytest.mark.parametrize(
    "move",
    [MagicMissile(), Drain(), Shield(), Poison(), Recharge()],
)
def test_move_spends_mana(move, initial_state):
    next_state = move.action().apply(initial_state)
    assert mana_points(next_state, Character.PLAYER) == 500 - move.mana_cost


def test_direct_damage_deals_damage(initial_state):
    move = DirectDamage()
    next_state = move.action().apply(initial_state)
    assert hit_points(next_state, Character.PLAYER) == 41


def test_magic_missile_deals_damage(initial_state):
    move = MagicMissile()
    next_state = move.action().apply(initial_state)
    assert hit_points(next_state, Character.BOSS) == 54


def test_drain_deals_damage_and_heals(initial_state):
    move = Drain()
    next_state = move.action().apply(initial_state)
    assert hit_points(next_state, Character.BOSS) == 56
    assert hit_points(next_state, Character.PLAYER) == 52


def test_shield_move_adds_shield_effect(initial_state):
    move = Shield()
    next_state = move.action().apply(initial_state)
    assert next_state.active_effects[-1] == EffectState(
        timer=6, effect=ShieldEffect(target=Character.PLAYER, armor=7)
    )


def test_poison_move_adds_poison_effect(initial_state):
    move = Poison()
    next_state = move.action().apply(initial_state)
    assert next_state.active_effects[-1] == EffectState(
        timer=6, effect=PoisonEffect(target=Character.BOSS, damage=3)
    )


def test_recharge_move_adds_recharge_effect(initial_state):
    move = Recharge()
    next_state = move.action().apply(initial_state)
    assert next_state.active_effects[-1] == EffectState(
        timer=5,
        effect=RechargeEffect(target=Character.PLAYER, recharge_amount=101),
    )
