from dataclasses import dataclass
from typing import Optional

from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effects import Effect


@dataclass(frozen=True)
class EffectState:
    effect: Effect
    timer: Optional[int] = None
    runs_on_turn: Optional[Character] = None
