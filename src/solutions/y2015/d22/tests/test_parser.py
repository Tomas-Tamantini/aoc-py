from src.solutions.y2015.d22.logic.parser.boss_stats import BossStats
from src.solutions.y2015.d22.logic.parser.parse_stats import parse_boss_stats


def test_parse_boss_stats(input_reader):
    reader = input_reader(
        """
        Damage: 8
        Hit points: 13
        """
    )
    stats = parse_boss_stats(reader)
    assert stats == BossStats(hit_points=13, damage=8)
