from src.solutions.y2021.d06.solution import lantern_fish_population


def test_lantern_fish_population_is_calculated_efficiently():
    initial_timers = (3, 4, 3, 1, 2)
    assert lantern_fish_population(initial_timers, days=18) == 26
    assert lantern_fish_population(initial_timers, days=256) == 26984457539
