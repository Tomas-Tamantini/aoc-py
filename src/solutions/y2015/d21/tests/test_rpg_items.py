from src.solutions.y2015.d21.logic.rpg_item import RpgItem, equip_fighter


def test_fighter_increments_damage_and_armor_with_items():
    items = [
        RpgItem(name="Sword", cost=10, damage=5, armor=0),
        RpgItem(name="Shield", cost=15, damage=0, armor=3),
        RpgItem(name="Helmet", cost=5, damage=0, armor=2),
    ]
    fighter = equip_fighter(hit_points=100, items=items)
    assert fighter.hit_points == 100
    assert fighter.damage == 5
    assert fighter.armor == 5
