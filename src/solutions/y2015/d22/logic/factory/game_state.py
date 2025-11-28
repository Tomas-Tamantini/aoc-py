from src.solutions.y2015.d22.logic.factory.characters import (
    initial_characters_state,
)
from src.solutions.y2015.d22.logic.factory.hard_mode_effect import (
    hard_mode_effect_state,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


def initial_state(easy_mode: bool, boss_hit_points: int) -> GameState:
    characters = initial_characters_state(boss_hit_points)
    if easy_mode:
        active_effects = tuple()
    else:
        active_effects = (hard_mode_effect_state(),)
    return GameState(characters=characters, active_effects=active_effects)
