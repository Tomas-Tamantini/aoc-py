from dataclasses import dataclass


@dataclass(frozen=True)
class IndicatorLightsDiagram:
    target_configuration: int
    buttons: set[int]
