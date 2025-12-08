from dataclasses import dataclass


@dataclass(frozen=True)
class Vector3D:
    x: int
    y: int
    z: int

    def distance_squared(self, other: "Vector3D") -> int:
        return (
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )
