import pytest

from src.solutions.y2015.d21.logic.fighter import Fighter
from src.solutions.y2015.d21.logic.rpg_game import player_wins


@pytest.mark.parametrize(
    ("player", "wins"),
    [
        (Fighter(hit_points=100, damage=8, armor=1), True),
        (Fighter(hit_points=100, damage=8, armor=0), False),
        (Fighter(hit_points=10, damage=10, armor=100), False),
    ],
)
def test_player_wins_if_boss_reaches_zero_hp_first(player, wins):
    boss = Fighter(hit_points=100, damage=8, armor=1)

    assert player_wins(player, boss) is wins
