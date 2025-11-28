from src.solutions.y2015.d22.logic.state.character import (
    Character,
    CharacterState,
)


def player() -> CharacterState:
    return CharacterState(id=Character.PLAYER, hit_points=50, mana_points=500)


def boss(boss_hit_points: int) -> CharacterState:
    return CharacterState(id=Character.BOSS, hit_points=boss_hit_points)


def initial_characters_state(
    boss_hit_points: int,
) -> tuple[CharacterState, CharacterState]:
    return (player(), boss(boss_hit_points))
