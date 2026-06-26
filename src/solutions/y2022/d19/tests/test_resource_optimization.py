import pytest

from src.solutions.y2022.d19.logic.blueprint import Blueprint
from src.solutions.y2022.d19.logic.resource import ResourceType
from src.solutions.y2022.d19.logic.resource_optimization import (
    maximize_resource,
)


def blueprint_1() -> Blueprint:
    return Blueprint(
        id=1,
        costs={
            ResourceType.ORE: {ResourceType.ORE: 4},
            ResourceType.CLAY: {ResourceType.ORE: 2},
            ResourceType.OBSIDIAN: {
                ResourceType.ORE: 3,
                ResourceType.CLAY: 14,
            },
            ResourceType.GEODE: {
                ResourceType.ORE: 2,
                ResourceType.OBSIDIAN: 7,
            },
        },
    )


def blueprint_2() -> Blueprint:
    return Blueprint(
        id=2,
        costs={
            ResourceType.ORE: {ResourceType.ORE: 2},
            ResourceType.CLAY: {ResourceType.ORE: 3},
            ResourceType.OBSIDIAN: {
                ResourceType.ORE: 3,
                ResourceType.CLAY: 8,
            },
            ResourceType.GEODE: {
                ResourceType.ORE: 3,
                ResourceType.OBSIDIAN: 12,
            },
        },
    )


@pytest.mark.parametrize(
    ("blueprint", "expected_max_geodes"),
    [(blueprint_1(), 9), (blueprint_2(), 12)],
)
def test_resource_gets_maximized(blueprint, expected_max_geodes):
    max_geodes = maximize_resource(
        resource_to_maximize=ResourceType.GEODE,
        time_limit=24,
        blueprint=blueprint,
        initial_fleet={ResourceType.ORE: 1},
    )
    assert max_geodes == expected_max_geodes
