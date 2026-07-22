from math import ceil

from src.solutions.y2015.d21.logic.fighter import Fighter


def _damage_per_round(fighter_a: Fighter, fighter_b: Fighter) -> int:
    return max(1, fighter_a.damage - fighter_b.armor)


def _hits_to_beat(fighter_a: Fighter, fighter_b: Fighter) -> int:
    return ceil(fighter_b.hit_points / _damage_per_round(fighter_a, fighter_b))


def player_wins(player: Fighter, boss: Fighter) -> bool:
    return _hits_to_beat(player, boss) <= _hits_to_beat(boss, player)
