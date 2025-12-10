from dataclasses import dataclass

type IndicatorLights = tuple[bool, ...]
type JoltageLevels = tuple[int, ...]
type ButtonWiring = tuple[int, ...]


@dataclass(frozen=True)
class Machine:
    target_indicator_lights: IndicatorLights
    target_joltage: JoltageLevels
    button_wirings: tuple[ButtonWiring, ...]

    @property
    def num_lights(self) -> int:
        return len(self.target_indicator_lights)
