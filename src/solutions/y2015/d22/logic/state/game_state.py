from dataclasses import dataclass

from src.solutions.y2015.d22.logic.state.character import CharacterState
from src.solutions.y2015.d22.logic.state.effect_state import EffectState


@dataclass(frozen=True)
class GameState:
    characters: tuple[CharacterState, CharacterState]
    active_effects: tuple[EffectState, ...] = tuple()
    next_character_idx: int = 0
    next_effect_idx: int = 0
