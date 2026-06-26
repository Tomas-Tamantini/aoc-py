import re
from typing import Iterator

from src.core.input_reader import InputReader
from src.solutions.y2022.d19.logic.blueprint import Blueprint
from src.solutions.y2022.d19.logic.resource import ResourceType

_RESOURCE_BY_NAME = {r.name.lower(): r for r in ResourceType}

_ROBOT_PATTERN = re.compile(r"Each (\w+) robot costs ([^.]+)\.?")
_COST_PATTERN = re.compile(r"(\d+) (\w+)")


def _parse_robot_costs(costs_str: str) -> dict[ResourceType, int]:
    return {
        _RESOURCE_BY_NAME[resource]: int(amount)
        for amount, resource in _COST_PATTERN.findall(costs_str)
    }


def _parse_blueprint(line: str) -> Blueprint:
    (bp_id,) = re.findall(r"Blueprint (\d+):", line)
    costs = {
        _RESOURCE_BY_NAME[robot]: _parse_robot_costs(costs_str)
        for robot, costs_str in _ROBOT_PATTERN.findall(line)
    }
    return Blueprint(id=int(bp_id), costs=costs)


def parse_blueprints(input_reader: InputReader) -> Iterator[Blueprint]:
    for line in input_reader.read_stripped_lines():
        yield _parse_blueprint(line)
