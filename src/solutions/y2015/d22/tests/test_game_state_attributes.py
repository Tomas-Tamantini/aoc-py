import pytest

from src.solutions.y2015.d22.logic.state.attributes import (
    current_effect_state,
    current_turn,
    is_over,
    player_won,
)
from src.solutions.y2015.d22.logic.state.character import Character


@pytest.mark.parametrize(
    ("boss_hp", "player_hp", "game_over"),
    [(1, 2, False), (1, 0, True), (0, 1, True)],
)
def test_game_is_over_if_some_player_died(
    state_with_hit_points, boss_hp, player_hp, game_over
):
    state = state_with_hit_points(player_hp, boss_hp)
    assert is_over(state) == game_over


@pytest.mark.parametrize(
    ("boss_hp", "won"), [(1, False), (0, True), (-1, True)]
)
def test_player_won_if_boss_died(state_with_hit_points, boss_hp, won):
    assert (
        player_won(state_with_hit_points(player_hp=10, boss_hp=boss_hp)) == won
    )


def test_current_effect_is_none_if_effect_pointer_is_outside_effects(
    initial_state_easy_mode,
):
    assert current_effect_state(initial_state_easy_mode) is None


def test_current_effect_is_the_one_in_current_pointer(
    initial_state_hard_mode, hard_mode_effect_state
):
    assert (
        current_effect_state(initial_state_hard_mode) == hard_mode_effect_state
    )


def test_current_turn_id_can_be_extracted(initial_state):
    assert current_turn(initial_state) == Character.PLAYER
