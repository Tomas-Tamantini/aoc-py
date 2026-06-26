from src.solutions.y2022.d19.logic.blueprint import Blueprint
from src.solutions.y2022.d19.logic.parser import parse_blueprints
from src.solutions.y2022.d19.logic.resource import ResourceType

BP1 = (
    "Blueprint 1: "
    "Each ore robot costs 2 ore. "
    "Each clay robot costs 4 ore. "
    "Each obsidian robot costs 4 ore and 15 clay. "
    "Each geode robot costs 2 ore and 15 obsidian."
)

BP2 = (
    "Blueprint 2: "
    "Each ore robot costs 4 ore. "
    "Each clay robot costs 4 ore. "
    "Each obsidian robot costs 4 ore and 12 clay. "
    "Each geode robot costs 3 ore and 8 obsidian."
)


def test_parse_blueprints(input_reader):
    reader = input_reader(
        f"""
        {BP1}
        {BP2}
        """
    )
    assert list(parse_blueprints(reader)) == [
        Blueprint(
            id=1,
            costs={
                ResourceType.ORE: {ResourceType.ORE: 2},
                ResourceType.CLAY: {ResourceType.ORE: 4},
                ResourceType.OBSIDIAN: {
                    ResourceType.ORE: 4,
                    ResourceType.CLAY: 15,
                },
                ResourceType.GEODE: {
                    ResourceType.ORE: 2,
                    ResourceType.OBSIDIAN: 15,
                },
            },
        ),
        Blueprint(
            id=2,
            costs={
                ResourceType.ORE: {ResourceType.ORE: 4},
                ResourceType.CLAY: {ResourceType.ORE: 4},
                ResourceType.OBSIDIAN: {
                    ResourceType.ORE: 4,
                    ResourceType.CLAY: 12,
                },
                ResourceType.GEODE: {
                    ResourceType.ORE: 3,
                    ResourceType.OBSIDIAN: 8,
                },
            },
        ),
    ]
