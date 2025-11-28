from typing import Optional

from src.solutions.y2015.d22.logic.state.character import (
    Character,
    CharacterState,
)
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import ShieldEffect
from src.solutions.y2015.d22.logic.state.game_state import GameState


def character_state(
    game_state: GameState, character: Character
) -> CharacterState:
    return next(c for c in game_state.characters if (c.id == character))


def current_turn(game_state: GameState) -> Character:
    return game_state.characters[game_state.next_character_idx].id


def hit_points(game_state: GameState, character: Character) -> int:
    return character_state(game_state, character).hit_points


def mana_points(game_state: GameState, character: Character) -> int:
    return character_state(game_state, character).mana_points


def available_mana(game_state: GameState) -> int:
    return mana_points(game_state, current_turn(game_state))


def armor(game_state: GameState, character: Character) -> int:
    for es in game_state.active_effects:
        if (
            isinstance(es.effect, ShieldEffect)
            and es.effect.target == character
        ):
            return es.effect.armor
    return 0


def is_over(game_state: GameState) -> bool:
    return any(c.hit_points <= 0 for c in game_state.characters)


def player_won(game_state: GameState) -> bool:
    return character_state(game_state, Character.BOSS).hit_points <= 0


def current_effect_state(game_state: GameState) -> Optional[EffectState]:
    if game_state.next_effect_idx < len(game_state.active_effects):
        return game_state.active_effects[game_state.next_effect_idx]


def opponent(character: Character) -> Character:
    return (
        Character.BOSS if character == Character.PLAYER else Character.PLAYER
    )
