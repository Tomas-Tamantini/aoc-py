from dataclasses import dataclass

from src.solutions.y2015.d22.logic.state.character import Character


class Effect: ...


@dataclass(frozen=True)
class HardModeEffect(Effect):
    target: Character
    damage: int


@dataclass(frozen=True)
class PoisonEffect(Effect):
    target: Character
    damage: int


@dataclass(frozen=True)
class RechargeEffect(Effect):
    target: Character
    recharge_amount: int


@dataclass(frozen=True)
class ShieldEffect(Effect):
    target: Character
    armor: int
