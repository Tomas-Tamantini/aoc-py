from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, Protocol

from src.solutions.y2015.d22.logic.actions.atomic import (
    AddTimedEffect,
    AtomicTransformation,
    DealDamage,
    Heal,
    ResetEffectPointer,
    SpendMana,
    ToggleTurn,
)
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.actions.game_action import GameAction
from src.solutions.y2015.d22.logic.state.attributes import (
    available_mana,
    opponent,
)
from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effects import (
    Effect,
    PoisonEffect,
    RechargeEffect,
    ShieldEffect,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


class GameMove(Protocol):
    def action(self) -> GameAction: ...

    def is_valid(self, game_state: GameState) -> bool: ...


@dataclass(frozen=True)
class _BaseMove(ABC):
    mana_cost: int = 0

    @abstractmethod
    def _specific_transformations(self) -> Iterator[AtomicTransformation]: ...

    @abstractmethod
    def _spell_caster(self) -> Character: ...

    def _transformations(self) -> Iterator[AtomicTransformation]:
        yield from self._specific_transformations()
        yield SpendMana(target=self._spell_caster(), mana_cost=self.mana_cost)
        yield ResetEffectPointer()
        yield ToggleTurn()

    def action(self) -> GameAction:
        return CompositeAction(tuple(self._transformations()), self.mana_cost)

    def is_valid(self, game_state: GameState) -> bool:
        return self.mana_cost <= available_mana(game_state)


@dataclass(frozen=True)
class DirectDamage(_BaseMove):
    damage: int = 9
    target: Character = Character.PLAYER

    def _spell_caster(self) -> Character:
        return opponent(self.target)

    def _specific_transformations(self) -> Iterator[AtomicTransformation]:
        yield DealDamage(self.target, self.damage)


@dataclass(frozen=True)
class MagicMissile(_BaseMove):
    target: Character = Character.BOSS
    damage: int = 4
    mana_cost: int = 53

    def _spell_caster(self) -> Character:
        return opponent(self.target)

    def _specific_transformations(self) -> Iterator[AtomicTransformation]:
        yield DealDamage(self.target, self.damage)


@dataclass(frozen=True)
class Drain(_BaseMove):
    target: Character = Character.BOSS
    damage: int = 2
    mana_cost: int = 73

    def _spell_caster(self) -> Character:
        return opponent(self.target)

    def _specific_transformations(self) -> Iterator[AtomicTransformation]:
        yield DealDamage(self.target, self.damage)
        yield Heal(self._spell_caster(), self.damage)


@dataclass(frozen=True)
class _BaseEffectMove(_BaseMove, ABC):
    duration: int = 1

    def _specific_transformations(self) -> Iterator[AtomicTransformation]:
        yield AddTimedEffect(effect=self._effect(), duration=self.duration)

    @abstractmethod
    def _effect(self) -> Effect: ...

    def _effect_is_active(self, game_state: GameState) -> bool:
        return any(
            e.effect == self._effect() for e in game_state.active_effects
        )

    def is_valid(self, game_state: GameState) -> bool:
        return self.mana_cost <= available_mana(
            game_state
        ) and not self._effect_is_active(game_state)


@dataclass(frozen=True)
class Shield(_BaseEffectMove):
    target: Character = Character.PLAYER
    armor: int = 7
    duration: int = 6
    mana_cost: int = 113

    def _spell_caster(self) -> Character:
        return self.target

    def _effect(self) -> Effect:
        return ShieldEffect(target=self.target, armor=self.armor)


@dataclass(frozen=True)
class Poison(_BaseEffectMove):
    target: Character = Character.BOSS
    damage: int = 3
    duration: int = 6
    mana_cost: int = 173

    def _spell_caster(self) -> Character:
        return opponent(self.target)

    def _effect(self) -> Effect:
        return PoisonEffect(target=self.target, damage=self.damage)


@dataclass(frozen=True)
class Recharge(_BaseEffectMove):
    target: Character = Character.PLAYER
    recharge_amount: int = 101
    duration: int = 5
    mana_cost: int = 229

    def _spell_caster(self) -> Character:
        return self.target

    def _effect(self) -> Effect:
        return RechargeEffect(
            target=self.target, recharge_amount=self.recharge_amount
        )
