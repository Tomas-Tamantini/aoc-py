from dataclasses import replace

import pytest

from src.solutions.y2015.d22.logic.actions.moves import (
    DirectDamage,
    Drain,
    MagicMissile,
    Poison,
    Recharge,
    Shield,
)
from src.solutions.y2015.d22.logic.auto.move_provider import AutoMoveProvider
from src.solutions.y2015.d22.logic.state.character import (
    Character,
    CharacterState,
)
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import (
    HardModeEffect,
    PoisonEffect,
    RechargeEffect,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


@pytest.fixture(scope="session")
def player_state():
    return CharacterState(id=Character.PLAYER, hit_points=50, mana_points=500)


@pytest.fixture(scope="session")
def boss_state():
    return CharacterState(id=Character.BOSS, hit_points=58)


@pytest.fixture(scope="session")
def hard_mode_effect():
    return HardModeEffect(target=Character.PLAYER, damage=1)


@pytest.fixture(scope="session")
def poison_effect():
    return PoisonEffect(target=Character.BOSS, damage=3)


@pytest.fixture(scope="session")
def recharge_effect():
    return RechargeEffect(target=Character.PLAYER, recharge_amount=101)


@pytest.fixture(scope="session")
def hard_mode_effect_state(hard_mode_effect):
    return EffectState(runs_on_turn=Character.PLAYER, effect=hard_mode_effect)


@pytest.fixture(scope="session")
def initial_state(player_state, boss_state):
    return GameState(characters=(player_state, boss_state))


@pytest.fixture(scope="session")
def initial_state_easy_mode(initial_state):
    return initial_state


@pytest.fixture(scope="session")
def initial_state_hard_mode(initial_state_easy_mode, hard_mode_effect_state):
    return replace(
        initial_state_easy_mode, active_effects=(hard_mode_effect_state,)
    )


@pytest.fixture
def state_with_hit_points(initial_state, player_state, boss_state):
    def _state(player_hp: int, boss_hp: int):
        return replace(
            initial_state,
            characters=(
                replace(player_state, hit_points=player_hp),
                replace(boss_state, hit_points=boss_hp),
            ),
        )

    return _state


@pytest.fixture(scope="session")
def state_with_effects(
    initial_state, hard_mode_effect, poison_effect, recharge_effect
):
    return replace(
        initial_state,
        active_effects=(
            EffectState(
                runs_on_turn=Character.PLAYER, effect=hard_mode_effect
            ),
            EffectState(timer=4, effect=poison_effect),
            EffectState(timer=1, effect=recharge_effect),
        ),
    )


@pytest.fixture(scope="session")
def hard_mode_state(state_with_effects):
    return state_with_effects


@pytest.fixture(scope="session")
def poison_state(state_with_effects):
    return replace(state_with_effects, next_effect_idx=1)


@pytest.fixture(scope="session")
def recharge_state(state_with_effects):
    return replace(state_with_effects, next_effect_idx=2)


@pytest.fixture(scope="session")
def player_moves():
    return [MagicMissile(), Drain(), Shield(), Poison(), Recharge()]


@pytest.fixture(scope="session")
def boss_moves():
    return [DirectDamage()]


@pytest.fixture(scope="session")
def move_provider(player_moves, boss_moves):
    return AutoMoveProvider(player_moves, boss_moves)
