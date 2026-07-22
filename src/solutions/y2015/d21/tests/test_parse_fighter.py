from src.solutions.y2015.d21.logic.parse_fighter import parse_fighter


def test_parse_fighter(input_reader):
    example = """Hit Points: 100
                 Damage: 8
                 Armor: 2"""
    reader = input_reader(example)
    fighter = parse_fighter(reader)
    assert fighter.hit_points == 100
    assert fighter.damage == 8
    assert fighter.armor == 2
