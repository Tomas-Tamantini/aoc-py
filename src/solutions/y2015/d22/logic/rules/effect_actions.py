from dataclasses import asdict
from typing import Iterator

from src.solutions.y2015.d22.logic.actions.atomic import (
    AtomicTransformation,
    DealDamage,
    DecrementEffectTimer,
    IncrementEffectPointer,
    RechargeMana,
    RemoveEffect,
)
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.actions.game_action import GameAction
from src.solutions.y2015.d22.logic.state.attributes import current_turn
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import (
    Effect,
    HardModeEffect,
    PoisonEffect,
    RechargeEffect,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


def _specific_transformations(
    effect: Effect,
) -> Iterator[AtomicTransformation]:
    if isinstance(effect, HardModeEffect) or isinstance(effect, PoisonEffect):
        yield DealDamage(**asdict(effect))
    elif isinstance(effect, RechargeEffect):
        yield RechargeMana(**asdict(effect))


def _effect_transformations(
    effect_state: EffectState, current_turn: Character
) -> Iterator[AtomicTransformation]:
    if effect_state.runs_on_turn is None or (
        effect_state.runs_on_turn == current_turn
    ):
        yield from _specific_transformations(effect_state.effect)
    if effect_state.timer is None:
        yield IncrementEffectPointer()
    elif effect_state.timer > 1:
        yield DecrementEffectTimer()
        yield IncrementEffectPointer()
    else:
        yield RemoveEffect()


def effect_action(game_state: GameState) -> GameAction:
    effect_state = game_state.active_effects[game_state.next_effect_idx]
    transformations = tuple(
        _effect_transformations(effect_state, current_turn(game_state))
    )
    return CompositeAction(transformations)
