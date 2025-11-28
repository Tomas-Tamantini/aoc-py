from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from typing import Iterator, Protocol

from src.solutions.y2015.d22.logic.state.attributes import armor
from src.solutions.y2015.d22.logic.state.character import (
    Character,
    CharacterState,
)
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import Effect
from src.solutions.y2015.d22.logic.state.game_state import GameState


class AtomicTransformation(Protocol):
    def apply(self, game_state: GameState) -> GameState: ...


@dataclass(frozen=True)
class ToggleTurn:
    @staticmethod
    def apply(game_state: GameState) -> GameState:
        next_idx = (game_state.next_character_idx + 1) % len(
            game_state.characters
        )
        return replace(game_state, next_character_idx=next_idx)


@dataclass(frozen=True)
class IncrementEffectPointer:
    @staticmethod
    def apply(game_state: GameState) -> GameState:
        return replace(
            game_state, next_effect_idx=game_state.next_effect_idx + 1
        )


@dataclass(frozen=True)
class ResetEffectPointer:
    @staticmethod
    def apply(game_state: GameState) -> GameState:
        return replace(game_state, next_effect_idx=0)


@dataclass(frozen=True)
class DecrementEffectTimer:
    @staticmethod
    def _updated_effect(effect_state: EffectState):
        if effect_state.timer is None:
            return effect_state
        else:
            return replace(effect_state, timer=effect_state.timer - 1)

    @staticmethod
    def _updated_effects(
        current_effect_idx: int, effect_states: tuple[EffectState, ...]
    ) -> Iterator[EffectState]:
        for i, effect in enumerate(effect_states):
            if i == current_effect_idx:
                yield DecrementEffectTimer._updated_effect(effect)
            else:
                yield effect

    @staticmethod
    def apply(game_state: GameState) -> GameState:
        effects = tuple(
            DecrementEffectTimer._updated_effects(
                game_state.next_effect_idx, game_state.active_effects
            )
        )
        return replace(game_state, active_effects=effects)


@dataclass(frozen=True)
class RemoveEffect:
    @staticmethod
    def apply(game_state: GameState) -> GameState:
        effs = game_state.active_effects
        idx = game_state.next_effect_idx
        new_effects = effs[:idx] + effs[idx + 1 :]
        return replace(game_state, active_effects=new_effects)


@dataclass(frozen=True)
class AddTimedEffect:
    effect: Effect
    duration: int

    def apply(self, game_state: GameState) -> GameState:
        new_effect_state = EffectState(effect=self.effect, timer=self.duration)
        return replace(
            game_state,
            active_effects=game_state.active_effects + (new_effect_state,),
        )


@dataclass(frozen=True)
class _UpdateCharacter(ABC):
    target: Character

    @abstractmethod
    def _update_character(
        self, character: CharacterState, game_state: GameState
    ) -> CharacterState: ...

    def _updated_characters(
        self, game_state: GameState
    ) -> Iterator[CharacterState]:
        for c in game_state.characters:
            if c.id == self.target:
                yield self._update_character(c, game_state)
            else:
                yield c

    def apply(self, game_state: GameState) -> GameState:
        characters = tuple(self._updated_characters(game_state))
        return replace(game_state, characters=characters)


@dataclass(frozen=True)
class DealDamage(_UpdateCharacter):
    damage: int

    def actual_damage(self, game_state: GameState) -> int:
        return max(1, self.damage - armor(game_state, self.target))

    def _update_character(
        self, character: CharacterState, game_state: GameState
    ) -> CharacterState:
        damage = self.actual_damage(game_state)
        return replace(character, hit_points=character.hit_points - damage)


@dataclass(frozen=True)
class Heal(_UpdateCharacter):
    hit_points_increment: int

    def _update_character(
        self, character: CharacterState, game_state: GameState
    ) -> CharacterState:
        return replace(
            character,
            hit_points=character.hit_points + self.hit_points_increment,
        )


@dataclass(frozen=True)
class RechargeMana(_UpdateCharacter):
    recharge_amount: int

    def _update_character(
        self, character: CharacterState, game_state: GameState
    ) -> CharacterState:
        return replace(
            character, mana_points=character.mana_points + self.recharge_amount
        )


@dataclass(frozen=True)
class SpendMana(_UpdateCharacter):
    mana_cost: int

    def _update_character(
        self, character: CharacterState, game_state: GameState
    ) -> CharacterState:
        return replace(
            character, mana_points=character.mana_points - self.mana_cost
        )
