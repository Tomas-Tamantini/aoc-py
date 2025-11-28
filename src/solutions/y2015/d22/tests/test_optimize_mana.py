import pytest

from src.solutions.y2015.d22.logic.auto.optimize_mana import min_mana_to_win


@pytest.mark.skip("Slow test (~5s)")
@pytest.mark.parametrize(
    ("fixture_name", "expected"),
    [("initial_state_easy_mode", 1269), ("initial_state_hard_mode", 1309)],
)
def test_minimum_mana_to_win_game_is_found(
    request, fixture_name, expected, move_provider
):
    initial_state = request.getfixturevalue(fixture_name)
    assert min_mana_to_win(initial_state, move_provider) == expected
